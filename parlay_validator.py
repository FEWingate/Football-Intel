"""
PARLAY_VALIDATOR.PY
====================
Deterministic check for a proposed N-team parlay's real combined odds
and payout. Same "Coeus proposes, a script verifies" principle as
dfs_lineup_validator.py — Coeus reasons about which legs to pick, this
function does the actual arithmetic, because trusting an LLM with
compounding multiplication across 3-7 real prices is exactly the kind
of silent-wrong-math failure that validator exists to prevent for DK
lineups, and the same risk applies here.

FanDuel odds come back from parlay-api.com in DECIMAL format,
confirmed directly against real API responses on 2026-09-05 (not
assumed from docs, which state American as the default — the real
FanDuel data disagreed with that default). All math below works in
decimal internally; American is only ever a display conversion.

REAL, IMPORTANT CAVEAT THIS VALIDATOR SURFACES RATHER THAN HIDES:
combined parlay odds are only correctly computed as the PRODUCT of each
leg's decimal price when the legs are truly independent. Two legs from
the SAME game are not independent — their outcomes correlate (e.g. a
QB throwing for over his passing-yards ladder and his team's total
going over are pushed by the same game script), so a real sportsbook's
actual same-game-parlay (SGP) price is not naive multiplication, it's
priced separately by FanDuel's own SGP engine, which this API does not
expose. This validator does NOT invent an SGP price. It flags any
parlay with 2+ legs sharing a canonical_event_id as "same_game_legs"
and reports the naive product ANYWAY, clearly labeled as a
cross-game-style estimate, not a real quoted SGP price — the report
must say this plainly rather than presenting a number that looks like
a real bookmaker quote when it isn't one.
"""

from collections import Counter


def decimal_to_american(d):
    """Standard, textbook conversion. d must be > 1.0 (a real decimal
    price always is — 1.0 would mean a bet that cannot possibly win)."""
    if d <= 1.0:
        raise ValueError(f"decimal odds must be > 1.0, got {d}")
    if d >= 2.0:
        return round((d - 1) * 100)
    return round(-100 / (d - 1))


def leg_key(leg):
    """Identity for duplicate-detection: same event, same market, same
    player/side. Two legs are the "same bet" if all three match, even
    if the line or price differs (e.g. a stale duplicate scrape)."""
    return (leg.get("canonical_event_id") or leg.get("event_id"),
            leg.get("market_key"), leg.get("player") or leg.get("side"))


def validate_parlay(legs, expected_size, stake=100):
    """legs: list of dicts, each with at least market_key, price
    (decimal), canonical_event_id (or event_id). expected_size: the
    declared N for this parlay (3, 4, 5, 6, or 7) — a real, checked
    fact, not just len(legs) trusted at face value.

    Returns (is_valid, errors, warnings, result) where result holds the
    real computed numbers (present even when is_valid is False, so a
    failing parlay's actual math is still visible for diagnosis)."""
    errors, warnings = [], []

    if len(legs) != expected_size:
        errors.append(f"Parlay declared as {expected_size}-team but has "
                       f"{len(legs)} legs.")

    keys = [leg_key(l) for l in legs]
    dupes = [k for k, n in Counter(keys).items() if n > 1]
    if dupes:
        errors.append(f"Duplicate leg(s) — same event/market/player appears "
                       f"more than once: {dupes}")

    prices = []
    for i, leg in enumerate(legs):
        price = leg.get("price")
        try:
            price = float(price)
        except (TypeError, ValueError):
            errors.append(f"Leg {i+1} has a missing or unparseable price: {price!r}")
            continue
        if price <= 1.0:
            errors.append(f"Leg {i+1} price {price} is not a valid decimal "
                           f"price (must be > 1.0).")
            continue
        prices.append(price)

    event_ids = [leg.get("canonical_event_id") or leg.get("event_id") for leg in legs]
    same_game_groups = [eid for eid, n in Counter(event_ids).items() if eid and n > 1]
    if same_game_groups:
        warnings.append(
            f"{len(same_game_groups)} game(s) contribute more than one leg to "
            f"this parlay: {same_game_groups}. The combined price below is a "
            f"naive cross-game-style product, NOT a real same-game-parlay "
            f"(SGP) quote — correlated same-game legs are not independent, "
            f"and this API does not expose FanDuel's actual SGP pricing.")

    result = None
    if prices and len(prices) == len(legs):
        combined_decimal = 1.0
        for p in prices:
            combined_decimal *= p
        combined_decimal = round(combined_decimal, 4)
        payout = round(stake * combined_decimal, 2)
        result = {
            "legs": len(legs),
            "combined_decimal": combined_decimal,
            "combined_american": decimal_to_american(combined_decimal),
            "stake": stake,
            "payout": payout,
            "profit": round(payout - stake, 2),
            "same_game_legs": bool(same_game_groups),
        }

    return (len(errors) == 0, errors, warnings, result)


def verify_legs_against_source(legs, real_props_by_key):
    """Cross-checks each proposed leg against the REAL source data —
    same principle as generate_weekly_dfs_report.py's
    enrich_lineup_with_game_info(): trust the real number from the
    data file over whatever Coeus wrote, in case of a transcription
    slip. real_props_by_key: dict keyed by leg_key(row) -> real row,
    built from the actual saved FanDuel props/odds data.

    Returns (verified_legs, mismatches) — verified_legs has each leg's
    price overwritten with the REAL price from source data wherever a
    match is found; mismatches lists legs that don't exist in the real
    data at all, which is a real problem (Coeus referenced a leg that
    isn't actually on the board), not a rounding difference to shrug off."""
    verified, mismatches = [], []
    for leg in legs:
        key = leg_key(leg)
        real = real_props_by_key.get(key)
        if real is None:
            mismatches.append(leg)
            verified.append(leg)  # keep as-is so validate_parlay still reports on it
            continue
        merged = dict(leg)
        merged["price"] = real.get("price", real.get("over_price"))
        merged["canonical_event_id"] = real.get("canonical_event_id")
        verified.append(merged)
    return verified, mismatches

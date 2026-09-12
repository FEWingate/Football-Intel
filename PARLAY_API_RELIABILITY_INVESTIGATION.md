# ParlayAPI FanDuel Player-Prop Reliability Investigation

Investigation date: 2026-09-12

## Classification

**Sustained upstream market-family reliability gap that must be treated as a
recurring operational risk.** The evidence does not support a Football Intel
parser defect or a request-shape defect. The observed incident lasted at least
37 minutes. More longitudinal samples are required to measure a recurrence
cadence. A retry may occasionally recover data, but retry-only handling is not
sufficient.

## Direct Evidence

At approximately 4:59 PM ET, the unchanged production request returned real
FanDuel passing-yard lines across multiple games. At approximately 5:15 PM ET,
an isolated request for only `player_passing_yards` and its ten milestone keys
returned HTTP 200 but zero real FanDuel passing-line coverage across 14 events.

A controlled repeat at 5:52 PM ET produced the following results:

| Request shape | Events returned | FanDuel events | Exact passing line | Any passing-family data |
|---|---:|---:|---:|---:|
| Standard hostname, no bookmaker filter | 14 | 0 | 0 | 0 |
| Standard hostname, `bookmakers=fanduel` | 0 | 0 | 0 | 0 |
| Recommended API hostname, FanDuel filter | 0 | 0 | 0 | 0 |
| Recommended hostname, one event ID | 0 | 0 | 0 | 0 |

Every response declared all 11 requested markets in `x-markets-served`, charged
11 credits in `x-requests-last`, and returned HTTP 200. Changing hostname,
bookmaker filtering, and event scope did not restore the market.

A five-market comparison at 5:53 PM ET returned 14 events and FanDuel data in
12 events, but all four plain line markets had zero coverage:

| Market | Events with FanDuel outcomes |
|---|---:|
| `player_passing_yards` | 0 |
| `player_rushing_yards` | 0 |
| `player_receiving_yards` | 0 |
| `player_receptions` | 0 |
| `player_anytime_touchdown_scorer` | 12 |

The flat `/props` endpoint was used only as an independent diagnostic. It had
5,000 total rows and 166 FanDuel rows, but passing and rushing data each covered
only one event; receiving and receptions each covered two. This confirms broad
partial ingestion rather than a passing-only request bug. It remains unsuitable
as Football Intel's production replacement for the reasons already documented.

## Provider Transparency Findings

- Live status reported FanDuel odds and props healthy while the market-level
  probes above were empty. The status signal is source-wide, not market-specific.
- The 24-hour status-history endpoint returned zero current samples and stated
  that its sampler had stopped writing. It cannot corroborate this incident.
- The public changelog contained no passing-yards or FanDuel NFL incident entry.
- Documentation warns that availability varies by source, sport, market, and
  time. It does not provide a per-market completeness or freshness guarantee.
- `/odds` supports `eventIds` and `bookmakers`; neither changed this result.

References:

- https://api.parlay-api.com/docs
- https://parlay-api.com/status
- https://parlay-api.com/changelog

## Required Mitigation

1. Never overwrite a recent, materially fuller market-family snapshot with an
   empty or catastrophically smaller HTTP 200 response.
2. Preserve recent last-known-good data by market family, not as an unqualified
   whole-file fallback.
3. Expose `current`, `stale_last_known_good`, or `unavailable` status with the
   original market timestamp and age. Never silently present stale lines as live.
4. Log safe per-market coverage counts plus `x-requests-last`,
   `x-markets-served`, and related headers for every build.
5. Retry only bounded transient failures. Do not repeatedly spend credits on an
   HTTP 200 response that continues to advertise served markets with zero rows.
6. Set `oddsFormat=decimal` explicitly because observed defaults have differed
   from the documentation.
7. Keep a backup-provider decision separate. The present evidence establishes
   the need for resilience but does not validate another source.

`investigate_parlay_passing_reliability.py` reproduces the safe coverage probes
without logging or storing the API key.

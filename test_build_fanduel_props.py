import sys
import types
import unittest
from datetime import datetime, timedelta, timezone


sys.modules.setdefault("requests", types.SimpleNamespace())

from build_fanduel_props import protect_against_coverage_collapse


def game(event_id, passing=None):
    return {
        "canonical_event_id": event_id,
        "player_props": {
            "passing_yards": passing or {},
            "rushing_yards": {},
            "receiving_yards": {},
            "receptions": {},
        },
        "anytime_td": [],
    }


def passing(player):
    return {
        player: {
            "line": {"point": 225.5, "over_price": 1.9, "under_price": 1.9},
            "alts": [],
        }
    }


class CoverageProtectionTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 9, 12, 22, 0, tzinfo=timezone.utc)

    def previous(self, age_minutes=10):
        generated = (self.now - timedelta(minutes=age_minutes)).isoformat()
        return {
            "generated_at": generated,
            "games": [game(str(index), passing(f"QB {index}")) for index in range(4)],
        }

    def test_recent_catastrophic_drop_carries_same_game_data(self):
        current = [game(str(index)) for index in range(4)]
        coverage, warnings = protect_against_coverage_collapse(
            current, self.previous(), self.now.isoformat()
        )

        self.assertEqual("stale_last_known_good", coverage["passing_yards"]["status"])
        self.assertEqual(4, coverage["passing_yards"]["carried_event_count"])
        self.assertEqual(4, coverage["passing_yards"]["displayed_event_count"])
        self.assertTrue(warnings)
        self.assertIn("QB 0", current[0]["player_props"]["passing_yards"])

    def test_old_data_expires_instead_of_being_carried(self):
        current = [game(str(index)) for index in range(4)]
        coverage, warnings = protect_against_coverage_collapse(
            current, self.previous(age_minutes=361), self.now.isoformat()
        )

        self.assertEqual("unavailable", coverage["passing_yards"]["status"])
        self.assertEqual(0, coverage["passing_yards"]["carried_event_count"])
        self.assertFalse(warnings)

    def test_non_catastrophic_partial_coverage_remains_current(self):
        current = [
            game("0", passing("Current QB 0")),
            game("1", passing("Current QB 1")),
            game("2", passing("Current QB 2")),
            game("3"),
        ]
        coverage, warnings = protect_against_coverage_collapse(
            current, self.previous(), self.now.isoformat()
        )

        self.assertEqual("current", coverage["passing_yards"]["status"])
        self.assertEqual(3, coverage["passing_yards"]["displayed_event_count"])
        self.assertEqual({}, current[3]["player_props"]["passing_yards"])
        self.assertFalse(warnings)

    def test_fallback_never_introduces_a_different_event(self):
        current = [game("new-1"), game("new-2")]
        coverage, warnings = protect_against_coverage_collapse(
            current, self.previous(), self.now.isoformat()
        )

        self.assertEqual("unavailable", coverage["passing_yards"]["status"])
        self.assertEqual(0, coverage["passing_yards"]["previous_event_count"])
        self.assertFalse(warnings)


class SuffixMergeTests(unittest.TestCase):
    def test_penix_plain_and_alts_merge(self):
        from build_fanduel_props import merge_suffix_duplicates
        line = {"point": 236.5, "over_price": 1.9, "under_price": 1.9}
        out = merge_suffix_duplicates({
            "Michael Penix": {"line": line, "alts": []},
            "Michael Penix Jr.": {"line": line, "alts": [{"threshold": 200}, {"threshold": 250}]},
            "Aaron Rodgers": {"line": line, "alts": []}})
        self.assertEqual(set(out), {"Michael Penix Jr.", "Aaron Rodgers"})
        self.assertEqual(len(out["Michael Penix Jr."]["alts"]), 2)
        self.assertEqual(out["Michael Penix Jr."]["line"], line)

    def test_known_name_wins(self):
        from build_fanduel_props import merge_suffix_duplicates
        b = {"line": None, "alts": []}
        out = merge_suffix_duplicates({"Brian Robinson": dict(b), "Brian Robinson Jr.": dict(b)}, {"Brian Robinson"})
        self.assertEqual(set(out), {"Brian Robinson"})


if __name__ == "__main__":
    unittest.main()


class ComboPropsTests(unittest.TestCase):
    def row(self, **kw):
        base = {"bookmaker": "fanduel", "market_key": "player_rush_reception_yds", "canonical_event_id": "e1",
                "player": "Christian McCaffrey", "line": 108.5, "over_price": 1.877, "under_price": 1.877,
                "period": "FULL", "last_update": "2026-10-19T19:17:00Z"}
        base.update(kw)
        return base

    def test_accepts_authentic_row_and_keeps_source_key(self):
        from build_fanduel_props import shape_combo_rows
        out = shape_combo_rows([self.row()], "2026-10-19T20:00:00+00:00")
        line = out["e1"]["rushing_receiving_yards"]["Christian McCaffrey"]["line"]
        self.assertEqual(line["point"], 108.5)
        self.assertEqual(line["source_market_key"], "player_rush_reception_yds")
        self.assertFalse(line["stale"])

    def test_rejects_bad_rows(self):
        from build_fanduel_props import shape_combo_rows
        bad = [self.row(bookmaker="draftkings"), self.row(market_key="player_brock_purdy___alt_passing_yds"),
               self.row(market_key="player_rush_yds"), self.row(period="1H"), self.row(line=None),
               self.row(line="n/a"), self.row(over_price=None, under_price=None), self.row(canonical_event_id=None)]
        self.assertEqual(shape_combo_rows(bad, "2026-10-19T20:00:00+00:00"), {})

    def test_carry_forward_marks_stale_and_stops_at_kickoff_or_six_hours(self):
        from build_fanduel_props import carry_combo_forward
        old_line = {"point": 108.5, "over_price": 1.877, "under_price": 1.877,
                    "fetched_at": "2026-10-19T19:00:00+00:00", "last_update": "x", "stale": False}
        prev = {"games": [{"canonical_event_id": "e1", "combo_props": {"rushing_receiving_yards": {"A B": {"line": old_line, "alts": []}}}}]}
        mk = lambda kick: [{"canonical_event_id": "e1", "commence_time": kick, "combo_props": {}}]
        g = mk("2026-10-20T00:15:00+00:00")
        cov = carry_combo_forward(g, prev, "2026-10-19T21:00:00+00:00")
        self.assertTrue(g[0]["combo_props"]["rushing_receiving_yards"]["A B"]["line"]["stale"])
        self.assertEqual(cov["rushing_receiving_yards"]["status"], "stale_last_known_good")
        g = mk("2026-10-19T20:00:00+00:00")                      # already kicked off
        carry_combo_forward(g, prev, "2026-10-19T21:00:00+00:00")
        self.assertEqual(g[0]["combo_props"]["rushing_receiving_yards"], {})
        g = mk("2026-10-20T10:00:00+00:00")                      # older than six hours
        cov = carry_combo_forward(g, prev, "2026-10-20T02:00:00+00:00")
        self.assertEqual(cov["rushing_receiving_yards"]["status"], "unavailable")

    def test_passing_rushing_is_always_unavailable(self):
        from build_fanduel_props import carry_combo_forward
        cov = carry_combo_forward([], None, "2026-10-19T21:00:00+00:00")
        self.assertEqual(cov["passing_rushing_yards"]["status"], "unavailable")

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


if __name__ == "__main__":
    unittest.main()

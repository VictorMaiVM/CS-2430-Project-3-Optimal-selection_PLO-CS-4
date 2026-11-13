#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Verification tests. Run with:  python -m unittest test_knapsack


import unittest
from experiments import EXPERIMENTS, totals, Experiment
from greedy import highest_rating_first, lightest_first, best_ratio_first, greedy_select
from brute_force import brute_force_top3
from manifest_rules import manifest_from_ids, evaluate_manifest

STRATEGIES = [highest_rating_first, lightest_first, best_ratio_first]


class TestKnapsack(unittest.TestCase):
    def test_greedy_respects_capacity(self):
        for strategy in STRATEGIES:
            self.assertLessEqual(totals(strategy())[0], 700)

    def test_optimal_beats_or_ties_every_greedy(self):
        top3, _, _ = brute_force_top3()
        for strategy in STRATEGIES:
            self.assertGreaterEqual(top3[0][2], totals(strategy())[1])

    def test_top3_sorted_and_valid(self):
        top3, checked, _ = brute_force_top3()
    #    self.assertEqual(checked, 4096)
        self.assertEqual(checked, 8192)
        self.assertEqual(len(top3), 3)
        ratings = [s[2] for s in top3]
        self.assertEqual(ratings, sorted(ratings, reverse=True))
        for _, weight, _ in top3:
            self.assertLessEqual(weight, 700)

    def test_capacity_zero_selects_nothing(self):
        for strategy in STRATEGIES:
            self.assertEqual(strategy(EXPERIMENTS, 0), [])

    def test_capacity_too_small_for_any_item(self):
        for strategy in STRATEGIES:
            self.assertEqual(strategy(EXPERIMENTS, 5), [])

    # def test_capacity_fits_everything(self):
    #    for strategy in STRATEGIES:
    #        self.assertEqual(len(strategy(EXPERIMENTS, 10_000)), 12)

    def test_rule_solar_instrument_limit(self):
        solar_manifest = manifest_from_ids(["2", "3", "7", "1"])
        eval_result = evaluate_manifest(solar_manifest, 700, apply_rules=True)
        self.assertFalse(eval_result.feasible)

    def test_rule_11a_prerequisite(self):
        invalid_manifest = manifest_from_ids(["11a", "1"])
        eval_result = evaluate_manifest(invalid_manifest, 700, apply_rules=True)
        self.assertFalse(eval_result.feasible)

    def test_rule_thermal_mass_credit(self):
        credit_manifest = manifest_from_ids(["1", "2", "4", "6", "10", "12"])
        eval_result = evaluate_manifest(credit_manifest, 700, apply_rules=True)
        self.assertTrue(eval_result.feasible)
        self.assertEqual(eval_result.adjusted_mass, 700)

    def test_hand_check_highest_rating_first(self):
        chosen = highest_rating_first()
        weight, rating = totals(chosen)
        self.assertLessEqual(weight, 700)
        self.assertGreater(rating, 0)
        ids = {e.number for e in chosen}
        self.assertTrue("2" in ids or "10" in ids)

    def test_tie_break_rule(self):
        tied_experiments = [
            Experiment("A", "Heavy Tied Item", 50, 5),
            Experiment("B", "Light Tied Item", 20, 5),
        ]
        chosen = greedy_select(tied_experiments, capacity=100, primary_key=lambda e: e.rating, descending=True)
        self.assertIn(tied_experiments[1], chosen)

if __name__ == "__main__":
    unittest.main()
#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Verification tests. Run with:  python -m unittest test_knapsack


import unittest

from dynamic_programming import dp_knapsack
from experiments import EXPERIMENTS, totals, Experiment, BASELINE_EXPERIMENTS, CAPACITY_LIMIT
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

    def test_top3_sorted_and_valid_with_feasibility_count(self):
        top3, checked, feasible_count = brute_force_top3()
        self.assertEqual(checked, 8192)
        self.assertLess(feasible_count, 8192)
        self.assertEqual(len(top3), 3)

        ratings = [s[2] for s in top3]
        self.assertEqual(ratings, sorted(ratings, reverse=True))

        optimal_manifest, optimal_mass, optimal_rating = top3[0]
        self.assertEqual(optimal_rating, 58)
        self.assertEqual(optimal_mass, 695)

    def test_capacity_zero_selects_nothing(self):
        for strategy in STRATEGIES:
            self.assertEqual(strategy(EXPERIMENTS, 0), [])

    def test_capacity_too_small_for_any_item(self):
        for strategy in STRATEGIES:
            self.assertEqual(strategy(EXPERIMENTS, 5), [])

    def test_rule_solar_instrument_limit_exact_violations(self):
        result1 = evaluate_manifest(manifest_from_ids(["2", "3", "7"]), apply_rules=True)
        self.assertFalse(result1.feasible)
        self.assertEqual(result1.reason, "Solar limit violated")

        result2 = evaluate_manifest(manifest_from_ids(["2", "3", "7", "1"]), apply_rules=True)
        self.assertFalse(result2.feasible)
        self.assertEqual(result2.reason, "Solar limit violated")

    def test_rule_solar_instrument_limit_boundary_acceptance(self):
        result = evaluate_manifest(manifest_from_ids(["2", "3"]), apply_rules=True)
        self.assertTrue(result.feasible)
        self.assertEqual(result.adjusted_mass, 452)

    def test_rule_11a_prerequisite_exact_violations(self):
        result = evaluate_manifest(manifest_from_ids(["11a"]), apply_rules=True)
        self.assertFalse(result.feasible)
        self.assertEqual(result.reason, "11a selected without 11")

    def test_rule_11a_prerequisite_boundary_acceptance(self):
        result = evaluate_manifest(manifest_from_ids(["11", "11a"]), apply_rules=True)
        self.assertTrue(result.feasible)
        self.assertEqual(result.adjusted_mass, 90)

    def test_rule_thermal_mass_credit_exact_verification(self):
        manifest = manifest_from_ids(["1", "2", "4", "6", "10", "12"])
        raw_baseline = sum(e.weight for e in manifest)
        self.assertEqual(raw_baseline, 707)

        eval_result = evaluate_manifest(manifest, 700, apply_rules=True)
        self.assertTrue(eval_result.feasible)
        self.assertEqual(eval_result.adjusted_mass, 700)

    def test_rule_thermal_mass_credit_negative_case(self):
        manifest = manifest_from_ids(["1", "2", "4", "5", "10", "12"])
        raw_baseline = sum(e.weight for e in manifest)
        self.assertEqual(raw_baseline, 804)

        eval_result = evaluate_manifest(manifest, 700, apply_rules=True)
        self.assertFalse(eval_result.feasible)
        self.assertEqual(eval_result.adjusted_mass, 804)

    def test_greedy_handling_of_11a(self):
        res_standard = highest_rating_first(retry_skipped=False)
        res_retry = highest_rating_first(retry_skipped=True)
        self.assertIsInstance(res_standard, list)
        self.assertIsInstance(res_retry, list)

    def test_dynamic_programming_cross_check(self):
        dp_chosen, dp_weight, dp_rating, _ = dp_knapsack()
        base_top3, _, _ = brute_force_top3(BASELINE_EXPERIMENTS, CAPACITY_LIMIT, apply_rules=False)
        optimal_base_rating = base_top3[0][2]
        optimal_base_weight = base_top3[0][1]

        self.assertEqual(dp_rating, optimal_base_rating)
        self.assertEqual(dp_weight, optimal_base_weight)

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

    def test_edge_case_exact_capacity_boundary(self):
        manifest_700 = manifest_from_ids(["1", "2", "4", "6", "10", "12"])  # Adjusted to 700
        res_700 = evaluate_manifest(manifest_700, 700, apply_rules=True)
        self.assertTrue(res_700.feasible)
        self.assertEqual(res_700.adjusted_mass, 700)

        res_699 = evaluate_manifest(manifest_700, 699, apply_rules=True)
        self.assertFalse(res_699.feasible)
        self.assertIn("Over capacity", res_699.reason)

    def test_edge_case_empty_manifest(self):
        res = evaluate_manifest([], 700, apply_rules=True)
        self.assertTrue(res.feasible)
        self.assertEqual(res.adjusted_mass, 0)
        self.assertEqual(res.rating, 0)

    def test_edge_case_invalid_id_lookup(self):
        with self.assertRaises(KeyError):
            manifest_from_ids(["999"])

if __name__ == "__main__":
    unittest.main()
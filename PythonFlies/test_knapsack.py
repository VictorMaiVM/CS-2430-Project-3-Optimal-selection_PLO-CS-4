#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Verification tests. Run with:  python -m unittest test_knapsack


import unittest
from experiments import EXPERIMENTS, totals
from greedy import highest_rating_first, lightest_first, best_ratio_first
from brute_force import brute_force_top3

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
        self.assertEqual(checked, 4096)
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

    def test_capacity_fits_everything(self):
        for strategy in STRATEGIES:
            self.assertEqual(len(strategy(EXPERIMENTS, 10_000)), 12)

    # TODO (Verification Lead): add a test that hand-checks one greedy result
    # against the assignment table, and a ties test for the tie-break rule.


if __name__ == "__main__":
    unittest.main()
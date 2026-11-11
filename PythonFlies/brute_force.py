#Team name:     Team 3
#Team members:  Dominique Frank, Vitor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Part 2 - exhaustive search over every possible selection, plus the
#required dynamic programming pseudocode (Part 4).

#With the revised manifest there are 13 experiments, so 2^13 = 8192 selections
#are checked. The count includes selections that break one or more rules; the
#shared evaluator (manifest.py) decides which are feasible.

#How the bitmask works: a number from 0 to 8191 written in binary has 13 bits.
#If bit i is 1, experiment i (by list position) is in the selection. Counting
#from 0 to 8191 visits every possible selection exactly once.


from experiments import EXPERIMENTS, CAPACITY_LIMIT, totals
from manifest_rules import evaluate_manifest


def brute_force_top3(experiments=EXPERIMENTS, capacity=CAPACITY_LIMIT,
                     apply_rules=True):
    #Check every selection and return (top3, selections_checked, feasible_count).

    #top3 is a list of up to 3 tuples: (chosen, adjusted_mass, total_rating),
    #best first. The first entry is the optimal feasible manifest.
    #apply_rules=False solves the original problem (capacity only).

    n = len(experiments)
    feasible = []
    selections_checked = 0

    for bitmask in range(2 ** n):
        selections_checked += 1
        # Pick experiment i whenever bit i of j is set.
        chosen = [experiments[i] for i in range(n) if bitmask & (1 << i)]
        result = evaluate_manifest(chosen, capacity, apply_rules)
        if result.feasible:
            feasible.append((chosen, result.adjusted_mass, result.rating))

    # Highest rating first, ties broken by lighter total weight.
    feasible.sort(key=lambda s: (-s[2], s[1]))
    return feasible[:3], selections_checked, len(feasible)

# ----------------------------------------------------------------------
# DYNAMIC PROGRAMMING PSEUDOCODE
#   solve small versions of the problem first and reuse their answers.
#
#   dp[i][w] = best total rating using only the first i experiments
#              with a weight limit of w kg.
#
#   Base case:  dp[0][w] = 0 for every w   (no experiments, no rating)
#
#   for i from 1 to n:
#       for w from 0 to CAPACITY:
#           if weight[i] > w:                  # item i cannot fit
#               dp[i][w] = dp[i-1][w]          # so skip it
#           else:                              # choose the better option:
#               skip = dp[i-1][w]
#               take = dp[i-1][w - weight[i]] + rating[i]
#               dp[i][w] = max(skip, take)
#
#   The optimal rating is dp[n][CAPACITY].
#   To find which experiments were chosen, backtrack from (n, CAPACITY):
#       if dp[i][w] != dp[i-1][w], experiment i was taken;
#       subtract its weight from w and continue to i-1.
#
# Cost: n * CAPACITY table cells = 12 * 700 = 8,400 steps, versus 4,096
# subsets here. DP wins as n grows: brute force doubles with every added
# item (2^n), while DP grows only linearly in n for a fixed capacity.
#Team name:     Team 3
#Team members:  Dominique Frank, Vitor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Part 2 - exhaustive search over all 2^12 = 4096 subsets, plus the
#required dynamic programming pseudocode.

#How the bitmask loop works: a number from 0 to 4095 written in binary has 12
#bits. If bit i is 1, experiment i is in the subset. Counting from 0 to 4095
#therefore visits every possible subset exactly once.


from experiments import EXPERIMENTS, CAPACITY, totals


def brute_force_top3(experiments=EXPERIMENTS, capacity=CAPACITY):
    #Check every subset and return (top3, subsets_checked, valid_count).

    #top3 is a list of up to 3 tuples: (chosen, total_weight, total_rating),
    #best first. The first entry is the optimal solution.

    n = len(experiments)
    valid = []
    subsets_checked = 0

    for bitmask in range(2 ** n):
        subsets_checked += 1
        # Pick experiment i whenever bit i of j is set.
        chosen = [experiments[i] for i in range(n) if bitmask & (1 << i)]
        weight, rating = totals(chosen)
        if weight <= capacity:
            valid.append((chosen, weight, rating))

    # Highest rating first, ties broken by lighter total weight.
    valid.sort(key=lambda s: (-s[2], s[1]))
    return valid[:3], subsets_checked, len(valid)

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
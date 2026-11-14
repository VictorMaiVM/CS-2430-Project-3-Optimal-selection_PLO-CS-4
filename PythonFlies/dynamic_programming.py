#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Part 4 (extra credit) - dynamic programming solution to the 0/1
#knapsack problem, plus a runtime comparison against brute force.
#This module solves the ORIGINAL 12-experiment problem (capacity only).
#The revised rules couple experiments together and are not enforced by this table.

#dp[i][w] = best total rating using only the first i experiments with a
#weight limit of w kg. Each cell makes one choice: skip experiment i, or take
#it (if it fits) and add its rating to the best answer for the remaining
#capacity. Every cell reuses answers already stored in the row above, so
#nothing is computed twice.

import time

from experiments import BASELINE_EXPERIMENTS, CAPACITY_LIMIT, totals
from brute_force import brute_force_top3


def dp_knapsack(experiments=BASELINE_EXPERIMENTS, capacity=CAPACITY_LIMIT):
    #Solve the knapsack with DP.

    #Returns (chosen, total_weight, total_rating, table) where table is the
    #full (n+1) x (capacity+1) DP table.

    n = len(experiments)

    # Row 0 is the base case: with no experiments, the best rating is 0.
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table one experiment (row) at a time.
    for i in range(1, n + 1):
        exp = experiments[i - 1]  # row i uses experiment i-1 (0-based list)
        for w in range(capacity + 1):
            skip = table[i - 1][w]  # best rating if we leave exp out
            if exp.weight > w:
                table[i][w] = skip  # does not fit, so skipping is forced
            else:
                take = table[i - 1][w - exp.weight] + exp.rating
                table[i][w] = max(skip, take)

    # Backtrack from the bottom-right cell to find which experiments were taken.
    chosen = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:  # value changed, so item i was taken
            exp = experiments[i - 1]
            chosen.append(exp)
            w -= exp.weight
    chosen.reverse()  # restore experiment-number order

    weight, rating = totals(chosen)
    return chosen, weight, rating, table


def compare_runtimes(repeats=20):
    #Time brute force and DP and print a short comparison.
    #Each is run `repeats` times and the average is reported in milliseconds.

    start = time.perf_counter()
    for _ in range(repeats):
        brute_force_top3(BASELINE_EXPERIMENTS, CAPACITY_LIMIT, apply_rules=False)
    brute_ms = (time.perf_counter() - start) / repeats * 1000

    start = time.perf_counter()
    for _ in range(repeats):
        dp_knapsack()
    dp_ms = (time.perf_counter() - start) / repeats * 1000

    n = len(BASELINE_EXPERIMENTS)
    print("=== BRUTE FORCE vs DYNAMIC PROGRAMMING ===")
    print(f"  Brute force: {brute_ms:8.2f} ms avg   work ~ 2^n = {2 ** n} subsets")
    print(f"  DP:          {dp_ms:8.2f} ms avg   work ~ n*W  = {n * CAPACITY_LIMIT} cells")
    print("  Brute force doubles with every added experiment; DP grows linearly")
    print("  in n (for a fixed capacity), so DP scales to much larger problems.")
    print("  Note: at n = 12 the two are close; the gap appears as n grows.\n")
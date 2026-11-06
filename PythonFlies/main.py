#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Run every part of the project and print all results.
#Usage:   python main.py


from greedy import highest_rating_first, lightest_first, best_ratio_first
from brute_force import brute_force_top3
from report_output import print_result, print_comparison
from dynamic_programming import dp_knapsack, compare_runtimes


def main():
    # Part 1: three greedy strategies.
    print("=========== PART 1: GREEDY STRATEGIES ===========\n")
    greedy_results = {
        "Highest Rating First": highest_rating_first(),
        "Lightest First": lightest_first(),
        "Best Rating/Weight Ratio": best_ratio_first(),
    }
    for name, chosen in greedy_results.items():
        print_result(name, chosen)

    # Part 2: brute force, top 3 valid subsets.
    print("=========== PART 2: BRUTE FORCE ===========\n")
    top3, checked, valid_count = brute_force_top3()
    print(f"Subsets examined: {checked}   Valid (<= 700 kg): {valid_count}\n")
    for rank, (chosen, weight, rating) in enumerate(top3, start=1):
        label = f"Rank {rank}" + (" (OPTIMAL)" if rank == 1 else "")
        print_result(label, chosen, weight, rating)

    # Part 3: comparison summary.
    print("=========== PART 3: COMPARISON ===========\n")
    print_comparison(greedy_results, top3[0][2])

    # Part 4: dynamic programming
    print("=========== PART 4: Dynamic Programming ===========\n")
    dp_chosen, dp_weight, dp_rating, _ = dp_knapsack()
    print_result("Dynamic Programming", dp_chosen, dp_weight, dp_rating)
    print(f"Matches brute-force optimum: {dp_rating == top3[0][2]}\n")
    compare_runtimes()


if __name__ == "__main__":
    main()
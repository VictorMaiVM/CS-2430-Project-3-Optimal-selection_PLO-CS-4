#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Part 3 - consistent, copy-friendly printing of every result and
#the comparison summary.

from experiments import totals


def print_result(label, chosen, weight=None, rating=None):
    #Print one solution: label, experiments, total weight, total rating.
    if weight is None or rating is None:
        weight, rating = totals(chosen)
    print(f"     ----------- {label} -----------")
    for e in chosen:
        print(f"  #{e.number:<2} {e.name:<27} {e.weight:>4} kg   rating {e.rating}")
    print(f"  Total weight: {weight} kg   Total rating: {rating}\n")


def print_comparison(greedy_results, optimal_rating):
    #Print which greedy strategies matched the brute-force optimum.

    #greedy_results: dict of {strategy name: chosen experiment list}

    print("----- COMPARISON SUMMARY -----")
    print(f"Brute-force optimal rating: {optimal_rating}")
    for name, chosen in greedy_results.items():
        weight, rating = totals(chosen)
        if rating == optimal_rating:
            verdict = "MATCHES OPTIMAL"
        else:
            verdict = f"DOES NOT MATCH (short by {optimal_rating - rating})"
        print(f"  {name:<28} weight {weight:>3} kg  rating {rating:>3}  {verdict}")
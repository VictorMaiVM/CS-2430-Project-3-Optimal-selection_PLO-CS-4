#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Part 3 - consistent, copy-friendly printing of every result and
#the comparison summary.

from experiments import totals
from manifest_rules import evaluate_manifest, manifest_from_ids

def ids_of(chosen):
    #Return a readable string of experiments IDs
    return ", ".join(e.number for e in chosen)


def print_result(label, chosen, adjusted_mass=None, rating=None):
    #Print one solution: IDs, baseline mass, adjusted mass, total rating.
    result = evaluate_manifest(chosen)
    if adjusted_mass is None:
        adjusted_mass = result.adjusted_mass
    if rating is None:
        rating = result.rating
    baseline, _ = totals(chosen)
    print(f"     ----------- {label} -----------")
    for e in chosen:
        print(f"  #{e.number:<3} {e.name:<29} {e.weight:>4} kg   rating {e.rating}")
    print(f"  IDs: {ids_of(chosen)}")
    print(f"  Baseline mass: {baseline} kg   Adjusted mass: {adjusted_mass} kg"
          f"   Total rating: {rating}\n")


def print_comparison(greedy_results, optimal_rating):
    #Print which greedy strategies matched the brute-force optimum.

    #greedy_results: dict of {strategy name: chosen experiment list}

    print("----- COMPARISON SUMMARY -----")
    print(f"Brute-force optimal rating: {optimal_rating}")
    for name, chosen in greedy_results.items():
        result = evaluate_manifest(chosen)
        if result.rating == optimal_rating:
            verdict = "MATCHES OPTIMAL"
        else:
            verdict = f"DOES NOT MATCH (short by {optimal_rating - result.rating})"
        print(f"  {name:<34} adj. mass {result.adjusted_mass:>3} kg  "
              f"rating {result.rating:>3}  {verdict}")
    print()


# Rule tests: (rule, candidate IDs, expected feasible, expected adjusted mass)
#  The first three come from the Change Request; the rest are
# extra cases showing each rule's boundary.
RULE_TESTS = [
    ("Solar limit", ["2", "3", "7"], False, 542),
    ("Solar limit", ["2", "3"], True, 452),
    ("11a prerequisite", ["11a"], False, 10),
    ("11a prerequisite", ["11", "11a"], True, 90),
    ("Thermal mass credit", ["1", "2", "4", "6", "10", "12"], True, 700),
    # 12 without 6 earns no credit, so this stays at its full 804 kg.
    ("Thermal mass credit", ["1", "2", "4", "5", "10", "12"], False, 804),
]


def run_rule_tests():
    #Run every rule test and print an expected-vs-actual table.
    #Returns True if all tests passed.

    print("=== RULE TESTS (expected vs. actual) ===")
    print(f"  {'Rule':<20} {'Candidate IDs':<28} {'Expected':<20} {'Actual':<20} Pass?")
    all_ok = True
    for rule, ids, exp_ok, exp_mass in RULE_TESTS:
        result = evaluate_manifest(manifest_from_ids(ids))
        expected = f"{'Accept' if exp_ok else 'Reject'}, {exp_mass} kg"
        actual = f"{'Accept' if result.feasible else 'Reject'}, {result.adjusted_mass} kg"
        ok = (result.feasible == exp_ok and result.adjusted_mass == exp_mass)
        all_ok = all_ok and ok
        print(f"  {rule:<20} {'{' + ', '.join(ids) + '}':<28} {expected:<20} "
              f"{actual:<20} {'PASS' if ok else 'FAIL'}")
    print()
    return all_ok
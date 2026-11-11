#Team name: Team 3
#Team members: Dominique Frank, Victor Mai, Erich Mundt
#Course: CS 2430 section 502
#Project: Programming Project 3

#Manifest evaluator used by both greedy and brute force
#algorithm solutions. "Revised rules" as follows:
# 1.Solar instrument limit. A manifest may include at most two
#   of Experiments 2, 3, and 7. Reject any candidate that selects all three.
# 2.Thermal mass credit. If both Experiments 6 and 12 are selected, subtract
#   7 kg from the candidate manifest’s total baseline mass. This reduces
# 3.Experiment 12’s charged mass from 27 kg to 20 kg. Experiment 6 still
#   contributes 7 kg, and both ratings contribute in full. Apply the credit once
#   , before checking the 700 kg limit. Experiment 11a prerequisite. A candidate
#   may include Experiment 11a only if it also includes Experiment 11. Experiment 11
#   can fly by itself. Together, the two packages contribute 90 kg and 12 science rating points

from collections import namedtuple

from experiments import CAPACITY_LIMIT, EXPERIMENTS

SOLAR_IDS = {"2", "3", "7"}
CREDIT_IDS = {"6", "12"}
CREDIT_KG = 7

Evaluation = namedtuple(
    "Evaluation", ["feasible", "adjusted_mass", "rating", "reason"]
)

def evaluate_manifest(chosen, capacity=CAPACITY_LIMIT, apply_rules=True):
    #Check canidate manifest
    #applies rules: False gives the Original problem(capacity check only),
    #which dynamic_programming.py uses
    #Returns an evaluation
    #Reason is "Ok" for a feasible manifest, otherwise it says which
    #rule has failed
    #adjusted mass and rating are always filled in, even for rejects

    ids = {e.number for e in chosen}
    adjusted_mass = sum(e.weight for e in chosen)
    rating = sum(e.rating for e in chosen)

    if not apply_rules:
        feasible = adjusted_mass <= capacity
        return Evaluation(feasible, adjusted_mass, rating,
                          "Ok" if feasible else "Over capacity")

    if CREDIT_IDS <= ids:
        return Evaluation(False, adjusted_mass, rating, "Solar limit violated")

    if "11a" in ids and "11" not in ids:
        return Evaluation(False, adjusted_mass, rating, "lla selected without 11")

    if adjusted_mass > capacity:
        return Evaluation(False, adjusted_mass, rating, f"Over capacity ({adjusted_mass} kg)")

    return Evaluation(True, adjusted_mass, rating, "Ok")

def manifest_from_ids(id_list, experiments=EXPERIMENTS):
    #Build a candidate manifest from experiment IDs
    lookup = {e.number: e for e in experiments}
    return [lookup[i] for i in id_list]
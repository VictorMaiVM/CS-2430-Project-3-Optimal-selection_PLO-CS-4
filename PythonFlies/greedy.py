#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Part 1 - three greedy strategies, updated for the revised rules.

#Each strategy ranks the experiments by a different rule, then walks down the
#ranked list. For EACH tentative addition it builds the resulting manifest and
#asks the shared evaluator (manifest.py) whether it is feasible, using
#ADJUSTED mass for the capacity check. Infeasible additions are skipped and
#scanning continues.

#RANKING RULES
#Highest Rating First : rating, largest first
#Lightest First       : baseline mass, smallest first
#Best Ratio First     : rating / baseline mass, largest first
#TIE-BREAK (all strategies): lighter baseline mass first, then the experiment's
#position in the manifest list (so 11 comes before 11a).

#EXPERIMENT 11a: if 11a is reached before 11 has been selected, adding it would
#break the prerequisite rule, so the evaluator rejects it and it is skipped.
#By default the scan never goes back, so 11a is lost for that run.


from experiments import EXPERIMENTS, CAPACITY_LIMIT, ratio
from manifest_rules import evaluate_manifest


def greedy_select(experiments, capacity, primary_key, descending, retry_skipped=False):
    #Build a payload greedily.

    #primary_key: function giving the value to sort on.
    #descending:  True to take largest values first, False for smallest first.
    #retry_skipped-True makes one extra pass over the skipped experiments in their
    #    original ranking order, which lets 11a in if 11 has been selected since.
    #Returns the list of chosen experiments (in the order they were added).

    position = {e.number: i for i, e in enumerate(experiments)}


    # Secondary keys (weight, number) always ascending, applied for ties.
    def sort_key(exp):
        primary = -primary_key(exp) if descending else primary_key(exp)
        return (primary, exp.weight, position[exp.number])

    ranked = sorted(experiments, key=sort_key)
    chosen = []
    skipped = []

    for exp in ranked:
        # Check the manifest as it WOULD be after adding this experiment.
        if evaluate_manifest(chosen + [exp], capacity).feasible:
            chosen.append(exp)
        else:
            skipped.append(exp)

    if retry_skipped:
        #One extra pass, same ranking order, over what was skipped.
        for exp in skipped:
            if evaluate_manifest(chosen + [exp], capacity).feasible:
                chosen.append(exp)

    return chosen


def highest_rating_first(experiments=EXPERIMENTS, capacity=CAPACITY_LIMIT,
                         retry_skipped=False):
    #Strategy 1: take the highest-rated experiments first.
    return greedy_select(experiments, capacity, lambda e: e.rating, True,
                         retry_skipped)

def lightest_first(experiments=EXPERIMENTS, capacity=CAPACITY_LIMIT,
                   retry_skipped=False):
    #Strategy 2: take the lightest experiments first.
    return greedy_select(experiments, capacity, lambda e: e.weight, False,
                         retry_skipped)

def best_ratio_first(experiments=EXPERIMENTS, capacity=CAPACITY_LIMIT,
                     retry_skipped=False):
    #Strategy 3: take the best rating/weight ratio first.
    return greedy_select(experiments, capacity, ratio, True, retry_skipped)
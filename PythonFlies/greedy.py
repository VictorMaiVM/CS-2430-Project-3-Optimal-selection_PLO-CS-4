#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Part 1 - three greedy strategies.
#Each strategy sorts the experiments by a different rule, then walks the
#sorted list and adds every experiment that still fits under the capacity.
#An experiment that does not fit is skipped (we keep scanning), so later,
#smaller experiments can still be added.

#TIE-BREAKING RULE: when two experiments tie
#on the primary sort value, the LIGHTER one comes first; if still tied, the
#LOWER experiment number comes first.


from experiments import EXPERIMENTS, CAPACITY_LIMIT, ratio


def greedy_select(experiments, capacity, primary_key, descending):
    #Build a payload greedily.

    #primary_key: function giving the value to sort on.
    #descending:  True to take largest values first, False for smallest first.
    #Returns the list of chosen experiments (in the order they were added).


    # Secondary keys (weight, number) always ascending, applied for ties.
    def sort_key(exp):
        primary = -primary_key(exp) if descending else primary_key(exp)
        return (primary, exp.weight, exp.number)

    chosen = []
    total_weight = 0
    for exp in sorted(experiments, key=sort_key):
        if total_weight + exp.weight <= capacity:
            chosen.append(exp)
            total_weight += exp.weight
    return chosen


def highest_rating_first(experiments=EXPERIMENTS, capacity=CAPACITY_LIMIT):
    #Strategy 1: take the highest-rated experiments first.
    return greedy_select(experiments, capacity, lambda e: e.rating, True)


def lightest_first(experiments=EXPERIMENTS, capacity=CAPACITY_LIMIT):
    #Strategy 2: take the lightest experiments first.
    return greedy_select(experiments, capacity, lambda e: e.weight, False)


def best_ratio_first(experiments=EXPERIMENTS, capacity=CAPACITY_LIMIT):
    #Strategy 3: take the best rating/weight ratio first.
    return greedy_select(experiments, capacity, ratio, True)
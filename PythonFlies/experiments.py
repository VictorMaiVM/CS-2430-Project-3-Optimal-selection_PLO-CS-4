#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 3

#Purpose: Shared data. Holds the 12 shuttle experiments and
#the weight capacity so every other module uses the same numbers.

from collections import namedtuple

# One candidate payload. 'number' matches the row number.
Experiment = namedtuple("Experiment", ["number", "name", "weight", "rating"])

# Shuttle payload limit in kilograms.
CAPACITY_LIMIT = 700

# The 12 experiments(indivisible items).
BASELINE_EXPERIMENTS = [
    Experiment(1, "Cloud Patterns", 36, 5),
    Experiment(2, "Solar Flares", 264, 9),
    Experiment(3, "Solar Power", 188, 6),
    Experiment(4, "Binary Stars", 203, 8),
    Experiment(5, "Relativity", 104, 8),
    Experiment(6, "Seed Viability", 7, 4),
    Experiment(7, "Sun Spots", 90, 2),
    Experiment(8, "Mice Tumors", 65, 8),
    Experiment(9, "Microgravity Plant Growth", 75, 5),
    Experiment(10, "Micrometeorites", 170, 9),
    Experiment(11, "Cosmic Rays", 80, 7),
    Experiment(12, "Yeast Fermentation", 27, 4),
]

#Revised manifest from the Change Request
REVISED_EXPERIMENTS = [
    Experiment("1", "Cloud Patterns", 36, 5),
    Experiment("2", "Solar Flares", 264, 9),
    Experiment("3", "Solar Power", 188, 6),
    Experiment("4", "Binary Stars", 203, 8),
    Experiment("5", "Relativity", 104, 8),
    Experiment("6", "Seed Viability", 7, 4),
    Experiment("7", "Sun Spots", 90, 2),
    Experiment("8", "Mice Tumors", 65, 8),
    Experiment("9", "Microgravity Plant Growth", 75, 5),
    Experiment("10", "Micrometeorites", 170, 9),
    Experiment("11", "Cosmic Rays (Primary Band)", 80, 7),
    Experiment("11a", "Cosmic Rays (Secondary Band)", 10, 5),
    Experiment("12", "Yeast Fermentation", 27, 4),
]

EXPERIMENTS = REVISED_EXPERIMENTS


def ratio(exp):
    #Return the rating-to-weight score (rating / weight) for an experiment.
    return exp.rating / exp.weight


def totals(chosen):
    #Return (total_weight, total_rating) for a list of experiments.
    return sum(e.weight for e in chosen), sum(e.rating for e in chosen)
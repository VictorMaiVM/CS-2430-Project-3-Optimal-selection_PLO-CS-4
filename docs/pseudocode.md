 Pseudocode: Programming Project 3 (Knapsack)

Capacity = 700 kg. There are 12 experiments, each with a number, name,
weight, and rating. Experiments are indivisible.

1. Shared data and helpers (experiments.py)


CONSTANT CAPACITY = 700
CONSTANT EXPERIMENTS = list of 12 (number, name, weight, rating) records

FUNCTION ratio(exp):
    RETURN exp.rating / exp.weight

FUNCTION totals(chosen):
    RETURN (sum of weights in chosen, sum of ratings in chosen)


2. Greedy strategies (greedy.py)

One helper does all the work. Each strategy only changes the ranking rule.
The shared evaluator (manifest_rules.py) decides whether a candidate manifest
is feasible: it applies the three revised rules and checks ADJUSTED mass
against the capacity.

FUNCTION greedy_select(experiments, capacity, primary_key, descending,
                       retry_skipped = FALSE):

    position = map from each experiment's ID to its index in the manifest list

    # Ranking rule, with tie-breaks
    sort experiments by:
        1. primary_key  (largest first if descending, else smallest first)
        2. baseline weight, lighter first
        3. position in the manifest list, earlier first   (11 before 11a)
    ranked = the sorted list

    chosen  = empty list
    skipped = empty list

    # Main pass: one scan down the ranked list
    FOR EACH exp IN ranked:
        candidate = chosen + [exp]
        IF evaluate_manifest(candidate, capacity) is feasible:
            add exp to chosen
        ELSE:
            add exp to skipped          # never revisited in the main pass

    # Optional retry pass (off by default)
    IF retry_skipped:
        FOR EACH exp IN skipped (in original ranking order):
            candidate = chosen + [exp]
            IF evaluate_manifest(candidate, capacity) is feasible:
                add exp to chosen

    RETURN chosen


The three strategies differ only in the arguments they pass:


FUNCTION highest_rating_first(...):
    RETURN greedy_select(experiments, capacity, rating,  descending = TRUE)

FUNCTION lightest_first(...):
    RETURN greedy_select(experiments, capacity, weight,  descending = FALSE)

FUNCTION best_ratio_first(...):
    RETURN greedy_select(experiments, capacity, rating / weight,
                         descending = TRUE)

Handling of Experiment 11a: if 11a is reached before 11 is in `chosen`, the
candidate manifest breaks the prerequisite rule, so the evaluator marks it
infeasible and 11a goes to `skipped`. The main pass never goes back, so 11a is
lost for that run. With retry_skipped = TRUE, one extra pass over `skipped`
lets 11a join if 11 has been selected since.


3. Brute-force search (brute_force.py)

Each number from 0 to 2^n - 1, written in binary, is one possible selection.
If bit i is 1, the experiment at list position i is in the selection. With the
revised manifest n = 13, so 2^13 = 8192 selections are checked, including
selections that break one or more rules. The shared evaluator
(manifest_rules.py) decides which are feasible.

FUNCTION brute_force_top3(experiments, capacity, apply_rules = TRUE):
    n = number of experiments                    (13)
    feasible = empty list
    selections_checked = 0

    FOR bitmask FROM 0 TO (2^n - 1):
        selections_checked = selections_checked + 1

        # Decode the bitmask into a list of experiments
        chosen = empty list
        FOR i FROM 0 TO n - 1:
            IF bit i of bitmask is 1:
                add experiments[i] to chosen

        # Apply the revised rules and the adjusted-mass capacity check
        result = evaluate_manifest(chosen, capacity, apply_rules)

        IF result is feasible:
            add (chosen, result.adjusted_mass, result.rating) to feasible

    sort feasible by rating (highest first),
         ties broken by lower adjusted mass

    RETURN first 3 entries of feasible,
           selections_checked,
           number of entries in feasible

The first entry returned is the optimal manifest. When apply_rules is FALSE,
the evaluator checks only the capacity, which solves the original
12-experiment problem (4096 selections) and is used to cross-check the
dynamic programming solution.

4. Output and comparison (report_output.py)


FUNCTION print_result(label, chosen, weight, rating):
    print label
    FOR EACH exp IN chosen:
        print number, name, weight, rating
    print total weight and total rating

FUNCTION print_comparison(greedy_results, optimal_rating):
    print optimal_rating
    FOR EACH (strategy_name, chosen) IN greedy_results:
        (weight, rating) = totals(chosen)
        IF rating == optimal_rating:
            verdict = "MATCHES OPTIMAL"
        ELSE:
            verdict = "DOES NOT MATCH" plus (optimal_rating - rating)
        print strategy_name, weight, rating, verdict


5. Main program (main.py)


PROCEDURE main:
    # Part 1
    greedy_results = {
        "Highest Rating First":     highest_rating_first(),
        "Lightest First":           lightest_first(),
        "Best Rating/Weight Ratio": best_ratio_first()
    }
    FOR EACH (name, chosen) IN greedy_results:
        print_result(name, chosen)

# Part 2
    (top3, checked, valid_count) = brute_force_top3()
    print checked and valid_count
    FOR rank FROM 1 TO 3:
        print_result("Rank " + rank, top3[rank])    # label rank 1 as OPTIMAL

# Part 3
    print_comparison(greedy_results, rating of top3[1])


6. Dynamic programming (concept; Part 4)


dp[i][w] = best total rating using only the first i experiments
           with a weight limit of w kg

Base case:  dp[0][w] = 0 for every w

FOR i FROM 1 TO n:
    FOR w FROM 0 TO CAPACITY:
        IF weight[i] > w:
            dp[i][w] = dp[i-1][w]                       # cannot fit, skip
        ELSE:
            skip = dp[i-1][w]
            take = dp[i-1][w - weight[i]] + rating[i]
            dp[i][w] = MAX(skip, take)

Optimal rating = dp[n][CAPACITY]

Backtrack to find the chosen experiments:
    w = CAPACITY
    FOR i FROM n DOWN TO 1:
        IF dp[i][w] != dp[i-1][w]:
            experiment i was taken
            w = w - weight[i]


Cost: DP fills n x CAPACITY cells (12 x 700 = 8,400), while brute force
examines 2^n subsets. Brute force doubles with every added item; DP grows
only linearly in n for a fixed capacity.
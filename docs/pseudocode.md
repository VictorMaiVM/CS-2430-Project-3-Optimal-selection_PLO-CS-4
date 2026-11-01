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

One helper does all the work. Each strategy only changes the sort rule.
FUNCTION greedy_select(experiments, capacity, primary_key, descending):
    sort experiments by:
        1. primary_key (largest first if descending, else smallest first)
        2. weight, lighter first          <- tie-break rule
        3. experiment number, lower first <- second tie-break

    chosen = empty list
    total_weight = 0

    FOR EACH exp IN sorted order:
        IF total_weight + exp.weight <= capacity:
            add exp to chosen
            total_weight = total_weight + exp.weight
        ELSE:
            skip exp and keep scanning    <- later, smaller items may still fit

    RETURN chosen

FUNCTION highest_rating_first():
    RETURN greedy_select(EXPERIMENTS, CAPACITY, rating, descending = TRUE)

FUNCTION lightest_first():
    RETURN greedy_select(EXPERIMENTS, CAPACITY, weight, descending = FALSE)

FUNCTION best_ratio_first():
    RETURN greedy_select(EXPERIMENTS, CAPACITY, ratio, descending = TRUE)


3. Brute-force search (brute_force.py)

Each number from 0 to 4095, written in binary, is one subset. If bit i is 1,
experiment i is included.


FUNCTION brute_force_top3(experiments, capacity):
    n = number of experiments            (12)
    valid_subsets = empty list
    subsets_checked = 0

    FOR mask FROM 0 TO (2^n - 1):
        subsets_checked = subsets_checked + 1
        chosen = empty list

        FOR i FROM 0 TO n - 1:
            IF bit i of mask is 1:
                add experiments[i] to chosen

        (weight, rating) = totals(chosen)

        IF weight <= capacity:
            add (chosen, weight, rating) to valid_subsets

    sort valid_subsets by rating (highest first),
        ties broken by lower total weight
    top3 = first 3 entries of valid_subsets

    RETURN top3, subsets_checked, number of valid_subsets


The first entry of top3 is the optimal solution.

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
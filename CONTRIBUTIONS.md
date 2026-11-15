# CONTRIBUTIONS

Team 3, CS 2430 section 502, Programming Project 3
Team members: Dominique Frank, Victor Mai, Erich Mundt
Repository: `<REPO URL>` (commit links use `<REPO URL>/commit/<hash>`)

Evidence below comes from the repository history (`git log --all`).

## Git author names
| Git author name | Team member |
|---|---|
| Wr3stl3r | Erich Mundt|
| DMF-Offb | Dominique Frank |
| Victor Mai | Victor Mai |

| Member | Role for Project 3 | Role in Project 2 |
|---|---|---|
| Dominique Frank | Communications Lead | Implementation Lead |
| Victor Mai | Verification Lead| **TO FILL** |
| Erich Mundt | Implementation Lead| Communications |

## Responsibilities and evidence

### Source code (`PythonFlies/`)

| Area | Author | Evidence (commit hashes) |
|---|---|---|
| Shared data (`experiments.py`: original 12 experiments, then revised manifest with 11a) | Wr3stl3r | de8f9fa (created), a4e4433 (revised experiments), d484b81 |
| Greedy strategies (`greedy.py`: `greedy_select`, `highest_rating_first`, `lightest_first`, `best_ratio_first`) | Wr3stl3r | 09cad06 (created), 3007075, f8ab90f (revised rules), eaed1aa |
| Brute force (`brute_force.py`: `brute_force_top3`) | Wr3stl3r | 9240950 (created), 3007075, 0e20483 (revised rules), b2e0ccf |
| Manifest evaluator (`manifest_rules.py`: `evaluate_manifest`, `manifest_from_ids`) | Wr3stl3r; Victor Mai | 0f93f9a (created, Wr3stl3r), f8ab90f (Wr3stl3r), ebcdae4 (Victor Mai: solar instrument limit fix), fa06f59 (Wr3stl3r) |
| Output and rule-test table (`report_output.py`: `print_result`, `print_comparison`, `run_rule_tests`) | Wr3stl3r | 30f0506 (created), fa2a509, 70929da, f3f6495 |
| Main program (`main.py`) | Wr3stl3r | 9e74070 (created), 944c56c, 0e20483, fa2a509, e1c45d4, 781df9b |
| Dynamic programming, extra credit (`dynamic_programming.py`: `dp_knapsack`, `compare_runtimes`) | Wr3stl3r | 944c56c (created), e1c45d4 |
| Tests (`test_knapsack.py`) | Wr3stl3r; Victor Mai | fe22c87 (created, Wr3stl3r), ebcdae4 (Victor Mai: updated tests for the change order), fa2a509 (Wr3stl3r: formatting) |

### Documentation and process

| Area | Author | Evidence |
|---|---|---|
| Repository layout and file stubs | Wr3stl3r | 83828cb |
| Project Plan (`docs/ProjectPlan.md`) | Wr3stl3r; DMF-Offb | b392624 (created, Wr3stl3r), 2a4ab5d and 5ec79e4 (Wr3stl3r: tasks marked done with commit numbers), 3e067b2, 65651dc, 4d44daf, 685dd80, 971c92d (DMF-Offb: uploads and moves of the plan file) |
| Design artifact 1: structure diagram (`docs/Stucture_Diagram`) | Wr3stl3r | b392624 |
| Design artifact 2: pseudocode (`docs/pseudocode.md`) | Wr3stl3r | a5f084f (created), eaed1aa, b2e0ccf, d484b81, fa06f59, 70929da, e1c45d4 (updated to match the current code) |
| README (`README.md`) | DMF-Offb | 1042ea8, 1407b5b, 8a847ee |
| Team report | DMF-Offb; Victor Mai | Programming Project 3: Report |
| Screencast | DMF-Offb | **TO FILL** (link or file name) |
| Final zip package and checks | DMF-Offb | **TO FILL** |

### Change Request work (Nov 9 to Nov 12)

| Task | Author | Evidence |
|---|---|---|
| Revised manifest with Experiment 11a | Wr3stl3r | a4e4433 |
| Rule logic in the evaluator | Wr3stl3r; Victor Mai | 0f93f9a, ebcdae4 |
| Greedy updated for rules and 11a handling | Wr3stl3r | f8ab90f |
| Brute force updated to 2^13 selections with rules | Wr3stl3r | 0e20483 |
| Rule tests (expected vs. actual) | Wr3stl3r; Victor Mai | ebcdae4, fa2a509 |


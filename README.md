# **CS 2430 – Programming Project 3**

## **The Knapsack Problem**

**Course:** CS 2430-502 – Fall 2026   
**Team Name:** Team 3 (Dominique Frank, Erich Mundt, Victor Mai)  
**Project Due Date:** November 15, 2026   
**Checkpoint Date:** November 8, 2026   
**Programming Language:** Python

## **1\. Project Overview** 

For Project 3, our team will be working on the 0/1 Knapsack Problem using Python. The goal is to find the best combination of scientific experiments that can fit within a 700 kg weight limit while getting the highest total rating possible. We will be using different algorithms to solve the problem and compare their results to see which approach works best.

## **2.Team 3 Members and Roles**

| Team Members | Role |
| ----- | ----- |
| Erich Mundt | Implementation Lead |
| Victor Mai | Verification Lead |
| Dominique Frank | Communication Lead |

## **3\. Project Requirements**

Our program will use Python to solve the 0/1 Knapsack Problem using four different approaches:

* Highest Rating First: Selects experiments with the highest ratings while staying within 700 kg.  
* Lightest First: Selects experiments with the lowest weights first.  
* Best Rating-to-Weight Ratio: Prioritizes experiments with the highest rating compared to their weight.  
* Brute Force: Checks all 4,096 possible combinations to find the three best valid solutions.

The program will display the selected experiments, total weights, and ratings for each method. We will compare the greedy algorithms against the optimal brute-force solution to see which performed best.

## **4\. Project Structure**

Our project is organized into separate Python files for the algorithms, experiment data, testing, and program output.

**Main Python Files**

**main.py**

The main program that runs the algorithms and displays the results.

**experiments.py**

Stores the scientific experiments and their weights and ratings.

**greedy.py**

Contains the three greedy strategies: Highest Rating First, Lightest First, and Best Rating-to-Weight Ratio.

**brute\_force.py**

Checks the possible combinations of experiments to find the highest-rated valid solutions.

**dynamic\_programming.py**

Contains the dynamic programming portion of the project.

**manifest\_rules.py**

Handles additional rules for the project.

**report\_output.py**

Organizes and displays the results from the algorithms.

**test\_knapsack.py**

Contains tests used to check the algorithms and verify their results.

## **5\. How to Run the Program**

With all Python files opened in your IDE:

* Open main.py.  
* Run the file using your IDE's Run option.  
* The program will automatically run all four parts:  
  * Three Greedy Strategies  
  * Brute Force  
  * Comparison Summary  
  * Dynamic Programming  
* The results will be displayed in the terminal.

Running the Tests

1. Open test\_knapsack.py.  
2. Run the file using your IDE's Run option.  
3. The terminal will display the test results and whether they passed or failed.

## **6\. Testing and Results**

Our program includes unit tests to check the algorithms and make sure the results follow the project requirements.

The tests cover:

* Making sure the greedy algorithms stay within the 700 kg weight limit.  
* Checking that the brute-force optimal rating is at least as high as the greedy results.  
* Checking that brute force returns three valid solutions in descending rating order.  
* Testing when the capacity is zero.  
* Testing when the capacity is too small for any experiment.  
* Testing when the capacity is large enough to fit all experiments.

The program also compares each greedy strategy against the brute-force optimal rating and displays whether it matches or falls short.

Dynamic programming is also included to compare its optimal rating against brute force and examine runtime differences.


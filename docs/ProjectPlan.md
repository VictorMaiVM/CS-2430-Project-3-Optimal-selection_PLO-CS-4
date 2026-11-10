# **CS 2430 – Programming Project 3**

## **Project Plan – The Knapsack Problem**

**Course:** CS 2430-502 – Fall 2026  
**Team Name:** Team 3  
**Project Due Date:** November 15, 2026  
**Checkpoint Date:** November 8, 2026  
**Programming Language:** Python

## **1\. Project Overview**

The goal of Project 3 is to solve the 0/1 Knapsack Problem using different algorithmic approaches. Our team will work with 12 scientific experiments that have different weights and ratings. We need to find the combination of experiments that gives the highest total rating without exceeding the space shuttle's 700 kg weight limit.

We will implement three greedy algorithms and a brute-force algorithm, compare their results, and explain which methods produce the best solutions.

## **2\. Team Roles and Responsibilities**

| Team Member | Role | Responsibilities |
| :---: | :---: | :---: |
| Dominique Frank | Communications Lead | Project documentation, report, README, Notes, and final submission |
| Erich | Implementation Lead | Programming, algorithm implementation, and code integration |
| Victor | Verification Lead | Testing, test plan, and correctness verification |

All members will contribute to the project and participate in the final screencast.

## **3\. Project Goals**

* Implement three greedy strategies: highest rating first, lightest weight first, and best rating-to-weight ratio.  
* Implement brute force to evaluate all 4,096 possible experiment combinations.  
* Identify the three highest-rated valid combinations.  
* Compare greedy results against the optimal brute-force solution.  
* Document the algorithms, results, and analysis in a formal report.  
* Include dynamic programming pseudocode, with the option to implement it for extra credit.

## **4\. Project Milestones**

### **Week 1 – Planning and Initial Development**

**Focus:** Set up the project and begin implementation.

* Assign team roles and responsibilities.  
* Create and organize the GitHub repository.  
* Complete the Project Plan.  
* Create two design artifacts for the checkpoint.  
* Begin implementing the greedy algorithms.  
* Start the README and team report outline.  
* Submit individual Weekly Status Reports.

### **Week 2 – Implementation, Testing, and Documentation**

**Focus:** Complete the required algorithms and collect results.

* Finish the three greedy strategies.  
* Implement brute force and identify the top three valid subsets.  
* Test algorithms and verify output accuracy.  
* Compare the greedy and optimal solutions.  
* Add results and analysis to the team report.  
* Update README and CONTRIBUTIONS.md.  
* Complete the applicable checkpoint requirements.

### **Final Phase – Review and Submission**

**Focus:** Finalize all project deliverables.

* Review and address the Canvas Change Request when released.  
* Complete any remaining testing and documentation.  
* Finalize the 3–5 page formal report.  
* Record the team screencast (10 minutes maximum).  
* Verify the source code and documentation package.  
* Submit the final report, ZIP, and screencast by November 15\.  
* Complete individual status reports and peer reviews as assigned.

## **5\. Task Assignment and Progress Tracking**

| Task | Owner | Status | Evidence |
| :---- | :---- | :---- | :---- |
| Create GitHub repository | Verification | Done | https\://github.com/VictorMaiVM/CS-2430-Project-3-Optimal-selection\_PLO-CS-4 |
| Create Project Plan | Communications | Done | docs/ProjectPlan.md |
| Create design documentation | Team | Done | commit\# b392624 |
| Develop three greedy algorithms | Implementation | Done | commit\# 09cad06 |
| Develop brute-force algorithm | Implementation | Done | commit\# 9240950 |
| Create test plan | Verification | Not Started | — |
| Test algorithms and record results | Verification | Done | commit\# fe22c87 |
| Prepare README | Communications | In Progress | docs/README.md |
| Prepare formal report | Communications / Team | In Progress | — |
| Update CONTRIBUTIONS.md | Communications / Team | Not Started | — |
| Record screencast | Team | Not Started | — |
| Prepare final submission | Communications | Not Started | — |

**Status Options:** Not Started / In Progress / Done / Blocked

## 

## **6\. Project Deliverables**

### **Checkpoint Requirements**

* Project Plan in /docs  
* Two design artifacts in /docs  
* Instructor viewer access to the repository

### **Final Requirements**

* Working source code implementing required algorithms  
* Completed formal team report (3–5 pages, excluding tables and appendices)  
* Finish the README that has build and run instructions  
* The CONTRIBUTIONS.md documenting team contributions  
* Completed testing documentation  
* Team screencast demonstrating the program less than 10 min  
* Final repository-exported ZIP file

**The formal report will be submitted separately from the ZIP file.**

## **7\. Communication and Collaboration**

We will mainly use Discord to communicate, discuss project progress, ask questions, and keep everyone updated. We’ll use GitHub to share code, organize documentation, and track our work throughout the project. Each person is responsible for updating everyone on tasks and issues you run into.

The Communications Lead will help keep the documentation organized, track progress, and make sure everything is ready for the final submission.

We will review code, and changes, test the program, and help each other out when needed to make sure we stay on track.

## 

## 

## **8\. Potential Risks and Solutions**

| Risk | Planned Solution |
| ----- | ----- |
| Algorithm produces incorrect results | Run verification tests and compare against brute force |
| Delays in implementation | Communicate progress and prioritize required features |
| GitHub merge conflicts | Coordinate changes and review pull requests |
| Incorrect or incomplete documentation | Review requirements before final submission |
| New functional requirement | Evaluate the change request and update the project plan |

## **9.Completion Criteria**

The project will be considered complete when all required algorithms execute correctly, the output is verified, all documentation is finished, and the final report, ZIP file, and screencast are ready for submission.
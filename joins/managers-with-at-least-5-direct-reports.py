# Write your MySQL query statement below
# ============================================
# Problem: Managers with at Least 5 Direct Reports
# Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
# ============================================

# Explanation:
# This problem combines:
# - GROUP BY
# - HAVING
# - SELF JOIN (same table used twice)
#
# Table:
# Employee(id, name, department, managerId)
#
# Goal:
# - Find managers who have at least 5 direct reports
# - Return manager names
#
# Key Idea:
# - Each employee has a managerId → tells who their manager is
# - So we count how many employees report to each manager
#
# Challenge:
# - managerId stores only ID, but we need manager NAME
# - So we must map managerId → Employee.id → Employee.name
#
# Why SELF JOIN?
# - One copy of table = employees
# - Another copy = managers
# - This allows us to connect employee → manager details
#
# Why GROUP BY + HAVING?
# - GROUP BY managerId → group all employees under each manager
# - COUNT(*) → number of direct reports
# - HAVING COUNT >= 5 → filter only required managers
#
# Optimization:
# - GROUP BY efficiently counts reports
# - JOIN retrieves manager names in same query
# - Time Complexity: O(n log n) depending on grouping
#
# How it works step-by-step:
# 1. Group employees by managerId
# 2. Count how many employees each manager has
# 3. Filter groups where count >= 5
# 4. JOIN with Employee table again to get manager names

# SQL Code:
SELECT e2.name
FROM Employee e1
JOIN Employee e2
ON e1.managerId = e2.id
GROUP BY e1.managerId
HAVING COUNT(e1.id) >= 5;

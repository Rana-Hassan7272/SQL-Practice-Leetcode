# ============================================
# Problem: Second Highest Salary
# Link: https://leetcode.com/problems/second-highest-salary/
# ============================================

# Explanation:
# This problem asks for the SECOND HIGHEST DISTINCT salary.
#
# Table:
# Employee(id, salary)
#
# Key Requirements:
# - DISTINCT salaries (duplicates ignored)
# - Return NULL if second highest does NOT exist
#
# Key Idea:
# - First remove duplicates → DISTINCT salary
# - Sort salaries in descending order
# - Skip the highest (OFFSET 1)
# - Take the next one (LIMIT 1)
#
# Why this approach?
# - Simple and efficient
# - Avoids complex window functions
# - OFFSET directly helps skip first value
#
# Important:
# - If no second highest exists → query returns empty
# - So we wrap it with IFNULL to return NULL explicitly
#
# Optimization:
# - DISTINCT reduces duplicates early
# - ORDER BY + LIMIT works efficiently with indexes
# - Time Complexity: O(n log n) (due to sorting)
#
# How it works step-by-step:
# 1. SELECT DISTINCT salary
# 2. ORDER BY salary DESC
# 3. Skip first row → OFFSET 1
# 4. Take next row → LIMIT 1
# 5. If no row → return NULL

# SQL Code:
SELECT 
    IFNULL(
        (SELECT DISTINCT salary
         FROM Employee
         ORDER BY salary DESC
         LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;

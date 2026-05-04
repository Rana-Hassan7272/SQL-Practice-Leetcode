# ============================================
# Problem: Department Top Three Salaries
# Link: https://leetcode.com/problems/department-top-three-salaries/
# ============================================

# Explanation:
# This is a HARD problem using:
# - JOIN
# - Window Functions (DENSE_RANK)
#
# Tables:
# Employee(id, name, salary, departmentId)
# Department(id, name)
#
# Goal:
# - For each department:
#     find employees whose salary is in TOP 3 UNIQUE salaries
#
# Key Challenge:
# - "Top 3 UNIQUE salaries" → duplicates should share same rank
# - Example:
#     90000 → rank 1
#     85000 → rank 2 (even if multiple employees)
#     70000 → rank 3
#
# Why DENSE_RANK()?
# - Assigns same rank to same salary
# - Does NOT skip ranks
#
# Difference:
# - RANK() → skips numbers (not suitable)
# - DENSE_RANK() → continuous ranking (perfect here)
#
# Why this approach?
# - Window functions allow ranking WITHOUT collapsing rows
# - Cleaner and more efficient than subqueries
#
# Optimization:
# - Single pass ranking per department
# - Efficient partitioning using PARTITION BY
#
# How it works step-by-step:
# 1. JOIN Employee with Department → get department names
# 2. Apply DENSE_RANK() partitioned by departmentId:
#    - Order salaries DESC
# 3. Assign rank to each employee
# 4. Filter where rank <= 3
# 5. Return required columns

# SQL Code:
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT *,
           DENSE_RANK() OVER (
               PARTITION BY departmentId
               ORDER BY salary DESC
           ) AS rnk
    FROM Employee
) e
JOIN Department d
ON e.departmentId = d.id
WHERE e.rnk <= 3;

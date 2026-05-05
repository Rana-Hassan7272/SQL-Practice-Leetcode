# ============================================
# Problem: Department Highest Salary
# Link: https://leetcode.com/problems/department-highest-salary/
# ============================================

# Explanation:
# We need to find employees who have the HIGHEST salary in each department.
#
# Tables:
# Employee(id, name, salary, departmentId)
# Department(id, name)
#
# Key Idea:
# - For each department, find the MAX salary
# - Then return employees whose salary matches that MAX
#
# Why this approach?
# - Uses GROUP BY + MAX() to compute highest salary per department
# - Then filters employees using that result
# - Handles ties automatically (multiple employees with same max salary)
#
# Steps:
# 1. Find max salary per department using GROUP BY
# 2. Join this result with Employee table
# 3. Match employee salary = max salary
# 4. Join Department table to get department name
#
# Optimization:
# - Aggregation reduces data early
# - Join ensures efficient filtering
# - Works well even for large datasets
#
# Alternative:
# - Can also be solved using DENSE_RANK() (window function)
# - But this approach is more commonly accepted in interviews

# SQL Code:
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
JOIN (
    SELECT 
        departmentId, 
        MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
) AS temp
    ON e.departmentId = temp.departmentId
    AND e.salary = temp.max_salary;

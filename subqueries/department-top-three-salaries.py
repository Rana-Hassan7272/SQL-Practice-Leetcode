# ============================================
# Problem: Department Top Three Salaries
# Link: https://leetcode.com/problems/department-top-three-salaries/
# ============================================

# Explanation:
# We need to find employees who are in the TOP 3 UNIQUE salaries per department.
#
# Tables:
# Employee(id, name, salary, departmentId)
# Department(id, name)
#
# Key Idea:
# - Use DENSE_RANK() to rank salaries within each department
# - Partition by departmentId → each department handled separately
# - Order by salary DESC → highest salary gets rank 1
#
# Why DENSE_RANK?
# - Handles duplicates correctly (same salary → same rank)
# - No gaps in ranking (important requirement)
#
# Example:
# Salaries: 90000, 85000, 85000, 70000
# DENSE_RANK → 1, 2, 2, 3
#
# Steps:
# 1. Assign rank to each employee inside their department
# 2. Keep only rank <= 3
# 3. Join with Department table to get department name
#
# Time Complexity:
# - Efficient due to window function optimization
#
# This is the MOST EXPECTED interview solution

# SQL Code:
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT 
        id,
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
        ) AS rnk
    FROM Employee
) e
JOIN Department d
    ON e.departmentId = d.id
WHERE e.rnk <= 3;

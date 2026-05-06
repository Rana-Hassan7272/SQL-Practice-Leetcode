# Write your MySQL query statement below
#LeetCode 1789 - Primary Department for Each Employee
#Link: https://leetcode.com/problems/primary-department-for-each-employee/

#explanation:
#- If employee has ONLY one department → return that department
#- If employee has MULTIPLE departments → return the one with primary_flag = 'Y'

#Steps:
#1. Count departments per employee using window function COUNT(*) OVER (PARTITION BY employee_id)
#2. Keep rows where:
#   - primary_flag = 'Y'  (multi-department case)
#   OR
#   - count = 1           (single department case)
#3. Return employee_id, department_id

#This is optimal because:
#- Uses window function → avoids subqueries
#- Single pass over data
#- O(n) complexity

#Pattern used:
#WINDOW COUNT → FILTER

SELECT 
    employee_id,
    department_id
FROM (
    SELECT 
        employee_id,
        department_id,
        primary_flag,
        COUNT(*) OVER (PARTITION BY employee_id) AS dept_count
    FROM Employee
) t
WHERE primary_flag = 'Y' 
   OR dept_count = 1;

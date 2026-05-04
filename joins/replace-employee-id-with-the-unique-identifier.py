# Write your MySQL query statement below
# ============================================
# Problem: Replace Employee ID With The Unique Identifier
# Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
# ============================================

# Explanation:
# This problem introduces JOINs (specifically LEFT JOIN).
#
# Tables:
# Employees(id, name)
# EmployeeUNI(id, unique_id)
#
# Goal:
# - Show unique_id and name for each employee
# - If employee does NOT have a unique_id → show NULL
#
# Key Idea:
# - We must keep ALL employees, even if they don't have a matching unique_id
#
# Why LEFT JOIN?
# - LEFT JOIN keeps all rows from the LEFT table (Employees)
# - If match is found in EmployeeUNI → show unique_id
# - If no match → NULL is returned automatically
#
# Why not INNER JOIN?
# - INNER JOIN would REMOVE employees without unique_id
# - But problem requires keeping them → so LEFT JOIN is correct
#
# Optimization:
# - JOIN on indexed column (id) → efficient lookup
# - No aggregation or subqueries → fast execution
#
# How it works step-by-step:
# 1. Start from Employees table
# 2. LEFT JOIN EmployeeUNI using id
# 3. For matched rows → unique_id appears
# 4. For unmatched rows → unique_id = NULL
# 5. Select required columns

# SQL Code:
SELECT 
    eu.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;

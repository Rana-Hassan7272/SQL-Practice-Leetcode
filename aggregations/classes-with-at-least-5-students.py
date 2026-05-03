# ============================================
# Problem: Classes With at Least 5 Students
# Link: https://leetcode.com/problems/classes-with-at-least-5-students/
# ============================================

# Explanation:
# This problem is about filtering groups based on a condition → classic HAVING use-case.
#
# Table:
# Courses(student, class)
#
# Goal:
# - Find classes that have at least 5 students.
#
# Key Idea:
# - GROUP BY class → group all students per class
# - COUNT(student) → count number of students in each class
# - HAVING → filter groups based on aggregate condition
#
# Why HAVING instead of WHERE?
# - WHERE filters rows BEFORE grouping
# - HAVING filters groups AFTER aggregation
# - Since COUNT() is an aggregate function, we MUST use HAVING
#
# Optimization:
# - GROUP BY partitions data efficiently
# - COUNT is computed per group
# - HAVING filters only required groups → avoids extra processing
# - Time Complexity: O(n)
#
# How it works step-by-step:
# 1. Group all rows by class.
# 2. For each class:
#    - Count number of students.
# 3. Apply HAVING condition:
#    - Keep only classes where count >= 5.
# 4. Return class names.

# SQL Code:
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;

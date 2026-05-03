# Write your MySQL query statement below
# ============================================
# Problem: Number of Unique Subjects Taught by Each Teacher
# Link: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
# ============================================

# Explanation:
# This problem introduces GROUP BY and aggregation.
#
# Table:
# Teacher(teacher_id, subject_id, dept_id)
#
# Key Observation:
# - A teacher may teach the SAME subject in multiple departments.
# - But we only count UNIQUE subjects per teacher.
#
# Example Insight:
# teacher_id = 1 teaches:
#   subject 2 in dept 3 and 4 → count as ONE subject
#   subject 3 → another subject
# Total = 2 unique subjects
#
# Why this approach?
# - GROUP BY teacher_id → groups all rows for each teacher
# - COUNT(DISTINCT subject_id) → counts only unique subjects
#
# Why DISTINCT is important?
# - Without DISTINCT, duplicate subject entries (due to multiple departments)
#   would incorrectly increase the count.
#
# Optimization:
# - GROUP BY efficiently partitions data
# - COUNT(DISTINCT ...) is optimized internally using hashing/sorting
# - Time Complexity: O(n log n) (depending on DB engine for distinct handling)
#
# How it works step-by-step:
# 1. Group rows by teacher_id.
# 2. For each group:
#    - Extract subject_id values.
#    - Remove duplicates using DISTINCT.
#    - Count remaining unique subjects.
# 3. Return teacher_id and count as 'cnt'.

# SQL Code:
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;

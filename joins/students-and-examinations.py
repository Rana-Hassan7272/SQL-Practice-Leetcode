# ============================================
# Problem: Students and Examinations
# Link: https://leetcode.com/problems/students-and-examinations/
# ============================================

# Explanation:
# This problem is about:
# - Generating ALL combinations (student × subject)
# - Counting occurrences (including 0 cases)
#
# Tables:
# Students(student_id, student_name)
# Subjects(subject_name)
# Examinations(student_id, subject_name)
#
# Goal:
# - For EACH student and EACH subject:
#     count how many times the student attended that exam
#
# Key Challenge:
# - Even if a student NEVER attended a subject → still show 0
#
# Key Idea:
# 1. CROSS JOIN → generate all possible (student, subject) pairs
# 2. LEFT JOIN → attach exam records if they exist
# 3. COUNT() → count how many matches found
#
# Why CROSS JOIN?
# - Ensures ALL combinations:
#   every student paired with every subject
#
# Why LEFT JOIN?
# - Keeps all combinations even if no exam exists
# - Missing matches → NULL → counted as 0
#
# Why COUNT(e.student_id)?
# - COUNT ignores NULL values
# - So it naturally counts only existing exam records
#
# Optimization:
# - CROSS JOIN creates base dataset (n * m)
# - LEFT JOIN attaches exam data efficiently
# - GROUP BY aggregates counts
#
# How it works step-by-step:
# 1. CROSS JOIN Students × Subjects → all combinations
# 2. LEFT JOIN Examinations:
#    - Match student_id AND subject_name
# 3. GROUP BY student_id, student_name, subject_name
# 4. COUNT how many times exam appears
# 5. ORDER BY student_id, subject_name

# SQL Code:
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
ON s.student_id = e.student_id
AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;

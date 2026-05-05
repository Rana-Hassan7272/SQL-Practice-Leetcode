# ============================================
# Problem: Consecutive Numbers
# Link: https://leetcode.com/problems/consecutive-numbers/
# ============================================

# Explanation:
# We need to find numbers that appear at least 3 times consecutively.
#
# Table:
# Logs(id, num)
#
# Key Idea (SELF JOIN approach):
# - Since id is auto-increment, consecutive rows have id difference = 1
# - So for 3 consecutive same numbers:
#     l1.id = x
#     l2.id = x + 1
#     l3.id = x + 2
#
# Strategy:
# - Join table with itself 3 times
# - Ensure:
#     l1.num = l2.num = l3.num
#     l1.id + 1 = l2.id
#     l2.id + 1 = l3.id
#
# Why this works:
# - We explicitly check 3 consecutive rows
# - No need for window functions
# - Very clear and interview-friendly logic
#
# Important:
# - Use DISTINCT to avoid duplicate outputs
#
# Time Complexity:
# - O(n) with indexing on id (efficient joins)
#
# Alternative:
# - Can also solve using LAG() window function (more modern SQL)
# - But self-join is classic and often expected

# SQL Code:
SELECT DISTINCT 
    l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 
    ON l1.id = l2.id - 1
JOIN Logs l3 
    ON l2.id = l3.id - 1
WHERE l1.num = l2.num 
  AND l2.num = l3.num;

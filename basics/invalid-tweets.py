# ============================================
# Problem: Invalid Tweets
# Link: https://leetcode.com/problems/invalid-tweets/
# ============================================

# Explanation:
# This problem is about identifying tweets whose content length exceeds a limit.
#
# Table:
# Tweets(tweet_id, content)
#
# Definition:
# - A tweet is INVALID if its content length > 15 characters.
#
# Key Idea:
# - Use LENGTH() function to count number of characters in content.
#
# Why this approach?
# - LENGTH() is a built-in SQL function optimized for string size calculation.
# - Direct filtering using WHERE avoids unnecessary complexity.
# - No joins, grouping, or subqueries required.
#
# Optimization:
# - Time Complexity: O(n) → scans each row once
# - LENGTH() is efficient and computed per row
# - Clean and minimal query → best practice
#
# How it works step-by-step:
# 1. For each row, calculate LENGTH(content).
# 2. Check if LENGTH(content) > 15.
# 3. If true → include that tweet_id.
# 4. Return only tweet_id column.

# SQL Code:
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;

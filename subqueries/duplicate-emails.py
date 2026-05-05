# ============================================
# Problem: Duplicate Emails
# Link: https://leetcode.com/problems/duplicate-emails/
# ============================================

# Explanation:
# We need to find emails that appear MORE THAN ONCE in the table.
#
# Table:
# Person(id, email)
#
# Key Idea:
# - Group rows by email
# - Count how many times each email appears
# - Keep only those emails where count > 1
#
# Why this approach?
# - GROUP BY groups identical emails together
# - COUNT(*) counts occurrences
# - HAVING filters aggregated results (very important)
#
# Important:
# - WHERE cannot be used with aggregate functions → use HAVING
# - DISTINCT is not needed because GROUP BY already ensures uniqueness
#
# Time Complexity:
# - O(n log n) depending on grouping (efficient for large datasets)
#
# Alternative:
# - Can also solve using self-join
# - But GROUP BY is simplest and most optimal

# SQL Code:
SELECT 
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;

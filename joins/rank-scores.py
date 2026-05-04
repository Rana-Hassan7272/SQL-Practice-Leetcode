# ============================================
# Problem: Rank Scores
# Link: https://leetcode.com/problems/rank-scores/
# ============================================

# Explanation:
# This problem is about ranking values with specific rules:
#
# Rules:
# 1. Higher score → better rank (DESC order)
# 2. Same score → same rank
# 3. No gaps in ranking (continuous ranks)
#
# Example:
# Scores: 100, 90, 90, 80
# Rank:     1,  2,  2,  3   ← NO gaps
#
# Key Insight:
# - We need ranking with:
#     ✔ same values → same rank
#     ✔ no skipped ranks
#
# Which function to use?
# - ROW_NUMBER() → ❌ wrong (always unique ranks)
# - RANK()       → ❌ wrong (creates gaps)
# - DENSE_RANK() → ✅ correct (no gaps, handles ties)
#
# Why DENSE_RANK()?
# - Assigns same rank to same scores
# - Ensures continuous ranking (no missing numbers)
#
# Why this approach?
# - Window functions allow ranking without grouping
# - Clean, efficient, and standard interview solution
#
# Optimization:
# - Single pass ranking → O(n log n) due to sorting
# - No joins or subqueries → optimal
#
# How it works step-by-step:
# 1. Sort scores in descending order
# 2. Apply DENSE_RANK() over ordered scores
# 3. Same scores → same rank
# 4. Next unique score → next consecutive rank

# SQL Code:
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;

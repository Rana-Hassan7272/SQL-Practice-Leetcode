# ============================================
# Problem: Queries Quality and Percentage
# Link: https://leetcode.com/problems/queries-quality-and-percentage/
# ============================================

# Explanation:
# This is a slightly advanced aggregation problem involving AVG, conditional logic,
# and percentage calculation.
#
# Table:
# Queries(query_name, result, position, rating)
#
# Definitions:
# 1. Quality:
#    - AVG(rating / position)
#
# 2. Poor Query Percentage:
#    - Percentage of queries where rating < 3
#    - Formula:
#      (count of rating < 3 / total count) * 100
#
# Key Idea:
# - GROUP BY query_name → process each query group separately
# - Use AVG() for quality
# - Use conditional COUNT via CASE WHEN for poor queries
#
# Why this approach?
# - AVG(rating / position) directly computes required metric
# - CASE WHEN allows counting only specific rows inside aggregation
# - Avoids subqueries → more efficient and readable
#
# Important Trick:
# - COUNT(CASE WHEN rating < 3 THEN 1 END)
#   counts only rows where condition is TRUE
#
# - Divide by COUNT(*) to get ratio
# - Multiply by 100 for percentage
#
# - ROUND(..., 2) ensures output is formatted to 2 decimal places
#
# Optimization:
# - Single pass aggregation using GROUP BY → O(n)
# - No joins or nested queries → efficient
#
# How it works step-by-step:
# 1. Group rows by query_name
# 2. For each group:
#    - Compute AVG(rating / position) → quality
#    - Count rows where rating < 3
#    - Divide by total rows → get fraction
#    - Multiply by 100 → percentage
# 3. Round both results to 2 decimal places

# SQL Code:
SELECT 
    query_name,
    ROUND(AVG(rating * 1.0 / position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;

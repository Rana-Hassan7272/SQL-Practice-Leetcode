# Write your MySQL query statement below
# ============================================
# Problem: Product Sales Analysis III
# Link: https://leetcode.com/problems/product-sales-analysis-iii/
# ============================================

# Explanation:
# This problem is about finding the FIRST occurrence (minimum year)
# for each product and then returning the full row(s) for that year.
#
# Table:
# Sales(sale_id, product_id, year, quantity, price)
#
# Goal:
# - For each product_id:
#     1. Find earliest year (MIN(year))
#     2. Return ALL rows for that product in that year
#
# Key Challenge:
# - We need both:
#     - Aggregation (MIN year)
#     - Full row data (quantity, price)
#
# Key Idea:
# - Use subquery to find MIN(year) per product
# - JOIN it back with original table to get full details
#
# Why this approach?
# - GROUP BY alone cannot return full row details correctly
# - JOIN ensures we only pick rows matching first year
#
# Optimization:
# - Subquery reduces data early (one row per product)
# - JOIN efficiently filters matching rows
# - Time Complexity: O(n log n) depending on grouping
#
# How it works step-by-step:
# 1. Subquery:
#    - GROUP BY product_id
#    - Find MIN(year) → first_year
#
# 2. JOIN:
#    - Match Sales with subquery using:
#        product_id
#        year = first_year
#
# 3. Select required columns:
#    - product_id
#    - first_year
#    - quantity
#    - price

# SQL Code:
SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) f
ON s.product_id = f.product_id
AND s.year = f.first_year;

# ============================================
# Problem: Big Countries
# Link: https://leetcode.com/problems/big-countries/
# ============================================

# Explanation:
# This is a basic filtering problem using SELECT and WHERE.
#
# Table:
# World(name, continent, area, population, gdp)
#
# Definition of "Big Country":
# A country is considered BIG if:
# 1. area >= 3000000
# OR
# 2. population >= 25000000
#
# Key Idea:
# - We just need to filter rows based on given conditions.
# - No joins, no grouping, no aggregation required.
#
# Why this approach?
# - Using WHERE clause is the most direct and optimal solution.
# - Conditions are simple comparisons → database can efficiently scan and filter.
# - Using OR ensures that even if ONE condition is satisfied, the row is included.
#
# Optimization:
# - Time Complexity: O(n) → single scan of table
# - If indexes exist on 'area' or 'population', filtering becomes faster.
# - Avoid unnecessary subqueries → keeps query clean and fast.
#
# How it works step-by-step:
# 1. Read each row from the World table.
# 2. Check:
#    - If area >= 3000000
#    - OR population >= 25000000
# 3. If any condition is TRUE → include that row.
# 4. Return only required columns: name, population, area.

# SQL Code:
SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;

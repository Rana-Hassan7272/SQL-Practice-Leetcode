# ============================================
# Problem: Seasonal Sales Analysis
# Link: https://leetcode.com/problems/seasonal-sales-analysis/
# ============================================

# Explanation:
# This is an ADVANCED aggregation + ranking problem involving:
# - JOIN
# - CASE WHEN (for seasons)
# - GROUP BY
# - SUM()
# - Window Function (ROW_NUMBER)
#
# Tables:
# sales(sale_id, product_id, sale_date, quantity, price)
# products(product_id, product_name, category)
#
# Goal:
# - For each season:
#     find the MOST popular category
#
# Popularity Rules:
# 1. Highest total quantity
# 2. If tie → highest revenue (quantity * price)
# 3. If still tie → lexicographically smaller category
#
# Key Idea:
# STEP 1 → Map each sale to a season
# STEP 2 → Aggregate total_quantity and total_revenue per (season, category)
# STEP 3 → Rank categories within each season
# STEP 4 → Pick top-ranked category per season
#
# Why use CASE WHEN?
# - To convert month → season (Winter, Spring, Summer, Fall)
#
# Why JOIN?
# - sales has product_id → need category from products table
#
# Why GROUP BY?
# - To calculate totals per (season, category)
#
# Why ROW_NUMBER()?
# - To rank categories within each season
# - ORDER BY:
#     quantity DESC
#     revenue DESC
#     category ASC (for lexicographical tie-break)
#
# Optimization:
# - Aggregation reduces dataset size early
# - Window function efficiently ranks within partitions
# - Clean and scalable solution
#
# How it works step-by-step:
# 1. Extract month from sale_date
# 2. Map month → season using CASE
# 3. JOIN sales with products → get category
# 4. GROUP BY season + category:
#    - SUM(quantity)
#    - SUM(quantity * price)
# 5. Apply ROW_NUMBER() partitioned by season:
#    - rank based on problem rules
# 6. Select rows where rank = 1

# SQL Code:
WITH season_data AS (
    SELECT 
        CASE 
            WHEN MONTH(s.sale_date) IN (12, 1, 2) THEN 'Winter'
            WHEN MONTH(s.sale_date) IN (3, 4, 5) THEN 'Spring'
            WHEN MONTH(s.sale_date) IN (6, 7, 8) THEN 'Summer'
            ELSE 'Fall'
        END AS season,
        p.category,
        SUM(s.quantity) AS total_quantity,
        SUM(s.quantity * s.price) AS total_revenue
    FROM sales s
    JOIN products p
    ON s.product_id = p.product_id
    GROUP BY season, p.category
),
ranked AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY season
            ORDER BY total_quantity DESC, total_revenue DESC, category ASC
        ) AS rn
    FROM season_data
)
SELECT 
    season,
    category,
    total_quantity,
    total_revenue
FROM ranked
WHERE rn = 1
ORDER BY season;

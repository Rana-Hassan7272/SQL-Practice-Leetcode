# ============================================
# Problem: 1164. Product Price at a Given Date
# Link: https://leetcode.com/problems/product-price-at-a-given-date/
# ============================================

# Approach:
# 1. For each product, rank price changes by date (latest first)
# 2. Keep only changes on/before '2019-08-16'
# 3. If no change exists before date → default price = 10
# 4. Pick the most recent change using ROW_NUMBER()

WITH ranked AS (
    SELECT 
        product_id,
        new_price,
        change_date,
        ROW_NUMBER() OVER (
            PARTITION BY product_id 
            ORDER BY change_date DESC
        ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
),

latest_prices AS (
    SELECT product_id, new_price
    FROM ranked
    WHERE rn = 1
),

all_products AS (
    SELECT DISTINCT product_id
    FROM Products
)

SELECT 
    p.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM all_products p
LEFT JOIN latest_prices lp
    ON p.product_id = lp.product_id;

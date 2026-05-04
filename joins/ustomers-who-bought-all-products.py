# ============================================
# Problem: Customers Who Bought All Products
# Link: https://leetcode.com/problems/customers-who-bought-all-products/
# ============================================

# Explanation:
# This is a classic "ALL vs COUNT" problem.
#
# Tables:
# Customer(customer_id, product_key)
# Product(product_key)
#
# Goal:
# - Find customers who bought ALL products available in Product table
#
# Key Idea:
# - For each customer:
#     count how many UNIQUE products they bought
# - Compare with:
#     total number of products in Product table
#
# If both counts are equal → customer bought ALL products
#
# Why DISTINCT?
# - Customer table may have duplicate rows
# - We only care about UNIQUE products per customer
#
# Why this approach?
# - Simple and efficient
# - Uses GROUP BY + HAVING
# - Avoids complex joins or subqueries per row
#
# Optimization:
# - COUNT(DISTINCT product_key) ensures correctness
# - Subquery (SELECT COUNT(*) FROM Product) runs once
# - Time Complexity: O(n)
#
# How it works step-by-step:
# 1. GROUP BY customer_id
# 2. For each customer:
#    - COUNT(DISTINCT product_key)
# 3. Get total product count from Product table
# 4. Compare both values using HAVING
# 5. Return customers where counts match

# SQL Code:
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*) FROM Product
);

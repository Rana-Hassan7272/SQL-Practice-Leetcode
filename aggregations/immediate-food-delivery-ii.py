# ============================================
# Problem: Immediate Food Delivery II
# Link: https://leetcode.com/problems/immediate-food-delivery-ii/
# ============================================

# Explanation:
# This is a MEDIUM level problem combining:
# - GROUP BY
# - MIN()
# - JOIN
# - Conditional aggregation
#
# Table:
# Delivery(delivery_id, customer_id, order_date, customer_pref_delivery_date)
#
# Definitions:
# - Immediate Order:
#     order_date == customer_pref_delivery_date
#
# - First Order:
#     Earliest order_date per customer
#
# Goal:
# - Find % of customers whose FIRST order was immediate
#
# Key Idea:
# STEP 1 → Find first order per customer
# STEP 2 → Check if that order is immediate
# STEP 3 → Compute percentage
#
# Why this approach?
# - Use subquery with MIN(order_date) to get first order per customer
# - Join back to original table to get full row details
# - Use CASE WHEN for conditional counting
#
# Optimization:
# - Subquery reduces dataset early
# - Join ensures accurate row matching
# - Single aggregation for percentage → efficient
#
# How it works step-by-step:
# 1. Subquery:
#    - GROUP BY customer_id
#    - Find MIN(order_date) → first order date
#
# 2. JOIN:
#    - Match original table with subquery
#    - Keep only rows that are first orders
#
# 3. For those rows:
#    - Check if order_date == customer_pref_delivery_date
#
# 4. Compute percentage:
#    - (immediate_count / total_first_orders) * 100
#
# 5. ROUND to 2 decimal places

# SQL Code:
SELECT 
    ROUND(
        SUM(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 
        / COUNT(*), 
    2) AS immediate_percentage
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) f
ON d.customer_id = f.customer_id
AND d.order_date = f.first_order_date;

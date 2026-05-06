# Write your MySQL query statement below
# LeetCode 183 - Customers Who Never Order
# Link: https://leetcode.com/problems/customers-who-never-order/

# explanation:
# - We need customers who do NOT appear in Orders table
# - This is a classic anti-join problem
# - Use LEFT JOIN and filter where Orders is NULL

# Steps:
# 1. LEFT JOIN Customers with Orders
# 2. Customers without orders will have NULL in Orders.customerId
# 3. Filter those rows

# This is optimal because:
# - Single join, no subquery overhead
# - Efficient with indexes
# - Standard anti-join pattern

# Pattern used:
# LEFT JOIN → NULL FILTER (ANTI-JOIN)

SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;

# Write your MySQL query statement below
#LeetCode - Products Ordered in a Given Period (Feb 2020 ≥ 100 units)
#Link: https://leetcode.com/problems/products-ordered-in-a-given-period/

#explanation:
#- We need products with TOTAL units >= 100 ONLY in Feb 2020
#- Filter Orders for date range Feb 2020
#- GROUP BY product_id → sum units
#- Keep only those with SUM(unit) >= 100
#- Join with Products to get product_name

#Steps:
#1. Filter orders WHERE order_date in Feb 2020
#2. GROUP BY product_id and SUM(unit)
#3. HAVING SUM(unit) >= 100
#4. JOIN with Products to get names

#This is optimal because:
#- Uses aggregation (GROUP BY) → minimal passes
#- No unnecessary subqueries
#- Index-friendly (on order_date, product_id)
#- O(n log n) grouping complexity

#Pattern used:
#FILTER → GROUP BY → HAVING → JOIN

SELECT 
    p.product_name,
    SUM(o.unit) AS unit
FROM Products p
JOIN Orders o
    ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;

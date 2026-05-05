# ============================================
# Problem: 1193. Monthly Transactions I
# Link: https://leetcode.com/problems/monthly-transactions-i/
# ============================================

# Window Function Approach:
# 1. Build monthly-country partition using DATE_FORMAT
# 2. Use SUM() and COUNT() OVER() for totals
# 3. Use conditional logic inside window functions

SELECT DISTINCT
    month,
    country,
    COUNT(*) OVER (PARTITION BY month, country) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END)
        OVER (PARTITION BY month, country) AS approved_count,
    SUM(amount) OVER (PARTITION BY month, country) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END)
        OVER (PARTITION BY month, country) AS approved_total_amount
FROM (
    SELECT 
        id,
        country,
        state,
        amount,
        DATE_FORMAT(trans_date, '%Y-%m') AS month
    FROM Transactions
) t;

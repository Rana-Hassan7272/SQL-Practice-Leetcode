# ============================================
# Problem: Customer Who Visited but Did Not Make Any Transactions
# Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
# ============================================

# Explanation:
# This problem involves identifying customers who visited but did NOT make any transactions.
#
# Tables:
# Visits(visit_id, customer_id)
# Transactions(transaction_id, visit_id)
#
# Key Idea:
# - Every transaction is linked to a visit_id.
# - If a visit_id from Visits does NOT appear in Transactions, it means no transaction was made.
#
# Why this approach?
# - We use LEFT JOIN because:
#   LEFT JOIN keeps ALL records from Visits
#   and matches records from Transactions where possible.
#
# - If there is NO match, columns from Transactions will be NULL.
# - That NULL indicates "no transaction happened".
#
# Optimization:
# - LEFT JOIN + NULL filtering is efficient and standard.
# - SQL engines optimize joins using indexes (if present on visit_id).
# - Avoids subqueries → better readability and performance.
#
# How it works step-by-step:
# 1. LEFT JOIN Visits with Transactions using visit_id.
# 2. Find rows where Transactions.visit_id IS NULL.
# 3. These rows represent visits with no transactions.
# 4. Group by customer_id to count such visits per customer.

# SQL Code:
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;

# ============================================
# Problem: Last Person to Fit in the Bus
# Link: https://leetcode.com/problems/last-person-to-fit-in-the-bus/
# ============================================

# Explanation:
# - People board the bus in order of "turn"
# - We maintain a RUNNING SUM of weights
# - Only allow rows where cumulative weight <= 1000
# - The LAST valid person is the answer

# Steps:
# 1. Compute cumulative weight using window function
#    SUM(weight) OVER (ORDER BY turn)
#
# 2. Filter rows where cumulative weight <= 1000
#
# 3. Return the person with highest turn among valid rows

# Pattern:
# WINDOW FUNCTION → FILTER → ORDER DESC → LIMIT 1

SELECT person_name
FROM (
    SELECT 
        person_name,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) AS q
WHERE cumulative_weight <= 1000
ORDER BY turn DESC
LIMIT 1;

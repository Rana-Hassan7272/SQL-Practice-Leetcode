# Write your MySQL query statement below
#LeetCode - Capital Gain/Loss
#Link: https://leetcode.com/problems/capital-gainloss/

#explanation:
#- Each Buy decreases capital, each Sell increases capital
#- Net capital gain/loss = SUM(Sell prices) - SUM(Buy prices)
#- Since every Buy has a matching Sell, we don't need pairing
#- Just treat:
#    Sell → +price
#    Buy  → -price

#Steps:
#1. Use CASE:
#   - If operation = 'Sell' → +price
#   - If operation = 'Buy'  → -price
#2. GROUP BY stock_name
#3. SUM all values → final gain/loss

#This is optimal because:
#- Single pass aggregation
#- No joins, no window functions needed
#- O(n) complexity (best possible)

#Pattern used:
#CONDITIONAL SUM (CASE WHEN)

SELECT 
    stock_name,
    SUM(
        CASE 
            WHEN operation = 'Sell' THEN price
            ELSE -price
        END
    ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;

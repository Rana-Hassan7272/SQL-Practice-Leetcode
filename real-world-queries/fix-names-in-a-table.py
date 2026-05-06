# Write your MySQL query statement below
#LeetCode 1667 - Fix Names in a Table
#Link: https://leetcode.com/problems/fix-names-in-a-table/

#explanation:
#- We need to normalize names:
#  -> first letter uppercase
#  -> rest lowercase
#- Use SQL string functions:
#  - UPPER(LEFT(name,1)) → first char uppercase
#  - LOWER(SUBSTRING(name,2)) → rest lowercase
#- Concatenate both parts
#- Order by user_id

#This is optimal because:
#- Single pass transformation
#- No joins or subqueries
#- O(n) complexity

#Pattern used:
#STRING MANIPULATION + CONCAT

SELECT 
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM Users
ORDER BY user_id;

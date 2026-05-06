# Write your MySQL query statement below
#LeetCode 196 - Delete Duplicate Emails
#Link: https://leetcode.com/problems/delete-duplicate-emails/

#explanation:
#- We must DELETE duplicate emails, keeping only the smallest id
#- For same email → keep MIN(id), delete others

#Steps:
#1. Self-join Person table:
#   - p1 joins p2 on same email
#   - p1.id > p2.id → means p1 is duplicate (higher id)
#2. Delete p1 rows

#This is optimal because:
#- Uses self join (no subqueries needed)
#- Efficient with index on email
#- O(n log n) join complexity

#Pattern used:
#SELF JOIN → DELETE DUPLICATES

DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;

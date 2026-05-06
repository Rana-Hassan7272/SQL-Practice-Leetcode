# Write your MySQL query statement below
#LeetCode 608 - Tree Node
#Link: https://leetcode.com/problems/tree-node/

#explanation:
#- Each node can be Root, Inner, or Leaf
#- Root → p_id IS NULL
#- Leaf → node does NOT appear as any p_id (no children)
#- Inner → node has parent AND also has children

#Steps:
#1. Check if p_id IS NULL → Root
#2. Else check if id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) → Leaf
#3. Else → Inner

#This is optimal because:
#- Single scan + subquery
#- No joins required
#- Efficient with indexing on id / p_id

#Pattern used:
#CASE WHEN + EXISTENCE CHECK

SELECT 
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree;

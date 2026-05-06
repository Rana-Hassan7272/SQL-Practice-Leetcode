# Write your MySQL query statement below
#LeetCode - Find Users with Persistent Behavior Patterns
#Link: https://leetcode.com/problems/find-users-with-persistent-behavior-patterns/

#explanation:
#Goal: find longest consecutive-day streak per (user_id, action)
#Condition:
#- same user
#- same action
#- consecutive dates (no gaps)
#- each row = exactly one action per day (given uniqueness)

#Core idea (window function trick):
#If dates are consecutive, then:
#   action_date - ROW_NUMBER() is constant
#So we create a "group key" to detect streaks.

#Steps:
#1. Assign row number per user+action ordered by date
#2. Compute diff: DATE_SUB(action_date, INTERVAL row_number DAY)
#3. Group by (user_id, action, diff) → each group = one streak
#4. Compute streak length using COUNT(*)
#5. Keep only streaks >= 5
#6. For each user, pick MAX streak
#7. Sort result

#This is optimal because:
#- Single pass window function
#- No self joins (important for performance)
#- O(n log n) due to ordering
#- Standard “consecutive sequence detection” pattern

#Pattern used:
#ROW_NUMBER + DATE SHIFT GROUPING (GAP IDENTIFICATION)

WITH ranked AS (
    SELECT 
        user_id,
        action,
        action_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, action 
            ORDER BY action_date
        ) AS rn
    FROM activity
),
streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM ranked
    GROUP BY 
        user_id,
        action,
        DATE_SUB(action_date, INTERVAL rn DAY)
),
filtered AS (
    SELECT *
    FROM streaks
    WHERE streak_length >= 5
),
best AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY streak_length DESC
           ) AS rnk
    FROM filtered
)

SELECT 
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM best
WHERE rnk = 1
ORDER BY streak_length DESC, user_id ASC;

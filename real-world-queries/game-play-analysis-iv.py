# Write your MySQL query statement below
# LeetCode 550 - Game Play Analysis IV
# Link: https://leetcode.com/problems/game-play-analysis-iv/

# explanation:
# - We need fraction of players who logged in again on the NEXT DAY after their FIRST login
# - First find each player's first login date
# - Then check if same player has activity on (first_date + 1 day)
# - Count such players and divide by total distinct players

# Steps:
# 1. Get first login date per player using MIN(event_date)
# 2. Join back with Activity to check next day login
# 3. Count players satisfying condition
# 4. Divide by total players and round to 2 decimal places

# This is optimal because:
# - Uses aggregation + join (no unnecessary window overhead)
# - Works efficiently with indexes on player_id
# - O(n log n) due to grouping

# Pattern used:
# FIRST VALUE → SELF JOIN → CONDITION CHECK → FRACTION

SELECT 
    ROUND(
        COUNT(DISTINCT a.player_id) / 
        (SELECT COUNT(DISTINCT player_id) FROM Activity)
    , 2) AS fraction
FROM Activity a
JOIN (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
) f
ON a.player_id = f.player_id
AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);

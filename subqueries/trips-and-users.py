# ============================================
# Problem: Trips and Users
# Link: https://leetcode.com/problems/trips-and-users/
# ============================================

# Explanation:
# We need to calculate DAILY cancellation rate for trips,
# but ONLY for trips where BOTH client and driver are NOT banned.
#
# Tables:
# Trips(id, client_id, driver_id, status, request_at)
# Users(users_id, banned, role)
#
# Key Idea:
# 1. Filter trips where BOTH client and driver are NOT banned
# 2. Group by date (request_at)
# 3. Compute:
#       cancellation_rate = cancelled_trips / total_trips
#
# What counts as "cancelled"?
# - status = 'cancelled_by_driver' OR 'cancelled_by_client'
#
# Why use CASE?
# - Helps count only cancelled trips inside aggregation
#
# Why ROUND?
# - Output requires 2 decimal places
#
# Why JOIN twice?
# - One join for client
# - One join for driver
#
# Steps:
# 1. Join Trips with Users (client + driver)
# 2. Filter banned = 'No' for both
# 3. Filter date range
# 4. GROUP BY date
# 5. Compute cancellation rate using SUM(CASE...)
#
# Time Complexity:
# - Efficient with proper indexing

# SQL Code:
SELECT 
    t.request_at AS Day,
    ROUND(
        SUM(
            CASE 
                WHEN t.status != 'completed' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
    2) AS `Cancellation Rate`
FROM Trips t
JOIN Users c 
    ON t.client_id = c.users_id
JOIN Users d 
    ON t.driver_id = d.users_id
WHERE c.banned = 'No'
  AND d.banned = 'No'
  AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;

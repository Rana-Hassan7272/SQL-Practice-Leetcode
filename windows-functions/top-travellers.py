# ============================================
# Problem: 1407. Top Travellers
# Link: https://leetcode.com/problems/top-travellers/
# ============================================

# Approach:
# 1. LEFT JOIN Users with Rides → to include users with no rides
# 2. SUM(distance) → total distance per user
# 3. Use IFNULL() → convert NULL to 0 (for users with no rides)
# 4. GROUP BY user
# 5. ORDER BY:
#    - travelled_distance DESC
#    - name ASC (tie breaker)

SELECT 
    u.name,
    IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r
    ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;

# ============================================
# Problem: 1141. User Activity for the Past 30 Days I
# Link: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
# ============================================

# Approach (Window Function Style):
# 1. Filter last 30 days → BETWEEN '2019-06-28' AND '2019-07-27'
# 2. Remove duplicates (same user multiple activities same day)
# 3. Use COUNT() OVER (PARTITION BY date) to count active users per day
# 4. Use DISTINCT to avoid repeated rows

SELECT DISTINCT
    activity_date AS day,
    COUNT(user_id) OVER (PARTITION BY activity_date) AS active_users
FROM (
    SELECT DISTINCT user_id, activity_date
    FROM Activity
    WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
) t;

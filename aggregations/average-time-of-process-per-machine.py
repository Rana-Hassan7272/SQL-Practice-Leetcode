# ============================================
# Problem: Average Time of Process per Machine
# Link: https://leetcode.com/problems/average-time-of-process-per-machine/
# ============================================

# Explanation:
# This problem involves pairing 'start' and 'end' records and then averaging durations.
#
# Table:
# Activity(machine_id, process_id, activity_type, timestamp)
#
# Key Challenge:
# - Each process has TWO rows:
#     1. start timestamp
#     2. end timestamp
# - We must compute: (end - start) for each process
# - Then average these durations per machine
#
# Key Idea:
# - Use SELF JOIN to pair 'start' and 'end' rows of the same process
#
# Why SELF JOIN?
# - Data is stored in rows (not columns)
# - start and end are separate rows → must combine them
#
# Join Conditions:
# - Same machine_id
# - Same process_id
# - One row is 'start', other is 'end'
#
# Why this approach?
# - Efficient way to align related rows
# - Avoids complex subqueries
# - Very common interview pattern (pairing rows)
#
# Optimization:
# - JOIN + GROUP BY → efficient processing
# - AVG() directly computes required value
# - Time Complexity: O(n log n) depending on join implementation
#
# How it works step-by-step:
# 1. Join Activity table with itself:
#    - a = start rows
#    - b = end rows
# 2. Match rows where:
#    - same machine_id and process_id
#    - a.activity_type = 'start'
#    - b.activity_type = 'end'
# 3. Compute duration:
#    - b.timestamp - a.timestamp
# 4. Group by machine_id
# 5. Take AVG of durations
# 6. Round result to 3 decimal places

# SQL Code:
SELECT 
    a.machine_id,
    ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
JOIN Activity b
ON a.machine_id = b.machine_id
AND a.process_id = b.process_id
AND a.activity_type = 'start'
AND b.activity_type = 'end'
GROUP BY a.machine_id;

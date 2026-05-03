# ============================================
# Problem: Article Views I
# Link: https://leetcode.com/problems/article-views-i/
# ============================================

# Explanation:
# This problem is about identifying authors who viewed their OWN articles.
#
# Table:
# Views(article_id, author_id, viewer_id, view_date)
#
# Key Observation:
# - If author_id == viewer_id → the author viewed their own article.
#
# Important Detail:
# - The table may contain duplicate rows.
# - We must return UNIQUE author ids.
#
# Why this approach?
# - Use WHERE to filter rows where author_id = viewer_id.
# - Use DISTINCT to remove duplicates (since table has no primary key).
# - Use ORDER BY to sort results in ascending order.
#
# Optimization:
# - Simple filtering → O(n) scan
# - DISTINCT may add slight overhead but necessary due to duplicates
# - No joins or subqueries → efficient and clean
#
# How it works step-by-step:
# 1. Scan each row in Views table.
# 2. Check if author_id == viewer_id.
# 3. Keep only those rows.
# 4. Remove duplicates using DISTINCT.
# 5. Rename column as 'id' (as required).
# 6. Sort result in ascending order.

# SQL Code:
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;

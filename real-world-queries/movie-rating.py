# Write your MySQL query statement below
#LeetCode 1341 - Movie Rating
#Link: https://leetcode.com/problems/movie-rating/

#explanation:
#We need TWO results:
#1. User with MAX number of ratings
#   - GROUP BY user_id
#   - COUNT ratings
#   - ORDER BY count DESC, name ASC (tie breaker)
#   - LIMIT 1

#2. Movie with HIGHEST AVG rating in Feb 2020
#   - Filter WHERE created_at in Feb 2020
#   - GROUP BY movie_id
#   - AVG(rating)
#   - ORDER BY avg DESC, title ASC (tie breaker)
#   - LIMIT 1

#Finally:
#- Combine both results using UNION ALL
#- Output column must be named "results"

#This is optimal because:
#- Uses aggregation only (COUNT, AVG)
#- Proper indexing on created_at improves performance
#- No unnecessary joins or nested heavy queries

#Pattern used:
#AGGREGATION → ORDER → LIMIT → UNION ALL

(
    SELECT u.name AS results
    FROM MovieRating mr
    JOIN Users u 
        ON mr.user_id = u.user_id
    GROUP BY mr.user_id
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1
)

UNION ALL

(
    SELECT m.title AS results
    FROM MovieRating mr
    JOIN Movies m 
        ON mr.movie_id = m.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mr.movie_id
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);

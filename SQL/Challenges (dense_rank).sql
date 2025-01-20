WITH challenge_count_ranked AS (
    SELECT 
        h.hacker_id,
        h.name,
        COUNT(*) AS challenge_count,
        DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS ranker,
        COUNT(*) OVER (PARTITION BY COUNT(*)) AS count_with_same_challenges
    FROM 
        hackers h
    JOIN 
        challenges c
    ON 
        h.hacker_id = c.hacker_id
    GROUP BY 
        h.hacker_id, h.name
)
SELECT 
    hacker_id,
    name,
    challenge_count
FROM 
    challenge_count_ranked
WHERE 
    count_with_same_challenges = 1 
    OR ranker = 1                 
ORDER BY 
    challenge_count DESC,
    hacker_id ASC;

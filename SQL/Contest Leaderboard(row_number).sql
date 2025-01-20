-- Rank submissions by score for each hacker and challenge
WITH ranked_scores AS (
    SELECT 
        h.hacker_id,
        h.name,
        ROW_NUMBER() OVER (
            PARTITION BY h.hacker_id, s.challenge_id 
            ORDER BY s.score DESC
        ) AS ranker,
        s.score
    FROM 
        hackers h
    JOIN 
        submissions s
    ON 
        h.hacker_id = s.hacker_id
)
-- Calculate total scores for each hacker
SELECT 
    hacker_id,
    name,
    SUM(score) AS total_score
FROM 
    ranked_scores
WHERE 
    ranker = 1
    AND score != 0
GROUP BY 
    hacker_id, name
ORDER BY 
    total_score DESC,
    hacker_id;

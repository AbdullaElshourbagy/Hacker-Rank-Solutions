----https://www.hackerrank.com/challenges/full-score/problem?h_r=next-challenge&h_v=zen


--Solution


SELECT h.hacker_id, h.name
FROM HACKERS H , SUBMISSIONS S , CHALLENGES C , DIFFICULTY D
where s.hacker_id = h.hacker_id
and s.challenge_id = c.challenge_id
and c.difficulty_level = d.difficulty_level
and s.score = d.score
GROUP BY h.hacker_id, h.name 
HAVING COUNT(*)>1 
ORDER BY COUNT(*) DESC, h.hacker_id;
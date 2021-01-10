----https://www.hackerrank.com/challenges/placements/problem


---Solution



SELECT s.Name
FROM Students s
INNER JOIN Friends f ON s.ID = f.ID
INNER JOIN Packages p1 ON p1.ID = s.ID
INNER JOIN Packages p2 ON p2.ID = f.Friend_ID
WHERE p2.Salary - p1.Salary > 0
ORDER BY p2.Salary;
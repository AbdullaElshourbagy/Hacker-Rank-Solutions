----https://www.hackerrank.com/challenges/the-blunder/problem


--Solution


SELECT ceil(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
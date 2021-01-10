--https://www.hackerrank.com/challenges/binary-search-tree-1/problem


--Solution


SELECT N || ' '||
(CASE
    WHEN P is NULL THEN 'Root'
    WHEN N in (SELECT P FROM BST) THEN 'Inner'
    ELSE 'Leaf'
END)
FROM BST
ORDER by N;
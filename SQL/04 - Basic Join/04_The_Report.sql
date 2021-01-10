---https://www.hackerrank.com/challenges/the-report/problem?h_r=next-challenge&h_v=zen


--Solution

SELECT 
(CASE WHEN grades.GRADE >=8 
THEN students.NAME
ELSE NULL
END)
,grades.GRADE, students.MARKS
FROM GRADES grades, STUDENTS students
WHERE students.MARKS BETWEEN grades.MIN_MARK AND grades.MAX_MARK
ORDER BY grades.GRADE DESC, students.NAME;
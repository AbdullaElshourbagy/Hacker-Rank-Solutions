--https://www.hackerrank.com/challenges/more-than-75-marks/problem


--Solution



Select Name from STUDENTS 
where Marks > 75
order by substr(Name,-3) ,ID asc;
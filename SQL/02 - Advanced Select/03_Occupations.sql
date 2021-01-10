---https://www.hackerrank.com/challenges/occupations/problem


--Solution



select doctor,professor,singer,actor
from ( select row_number() over(partition by Occupation order by Name) ro,
      Name as name,Occupation as occ from OCCUPATIONS ) data
pivot
(max(name)
 for occ in ('Doctor' as doctor,'Actor' as actor,'Professor' as professor,'Singer' as singer))
 order by ro asc;
--https://www.hackerrank.com/challenges/print-prime-numbers/problem


--Solution

with tempa as
(
  select level as Num
  from dual
  connect by level<=1000
),
tempb as
(
    select a.NUm,b.Num as Num_1
    from tempa a , tempa b
    where b.Num<=a.Num
),
tempc as
(
    select Num, sum(case when mod(num,num_1)=0 then 1 end) as Factor_COunt
    from tempb
    group by Num
)
select listagg(Num,'&') within group (order by Num)
from tempc
where Factor_COunt=2
;
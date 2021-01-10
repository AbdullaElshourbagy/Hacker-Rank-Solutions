--https://www.hackerrank.com/challenges/weather-observation-station-11/problem

--Solution



SELECT DISTINCT CITY FROM STATION WHERE not REGEXP_LIKE (UPPER(city),'^[AEIOU].*[AEIOU]$');


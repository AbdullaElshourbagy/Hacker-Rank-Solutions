--https://www.hackerrank.com/challenges/weather-observation-station-12/problem

--Solution

SELECT DISTINCT CITY FROM STATION WHERE  REGEXP_LIKE(UPPER(city), '^[^AEIOU].*[^AEIOU]$');

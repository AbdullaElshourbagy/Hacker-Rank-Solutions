--https://www.hackerrank.com/challenges/weather-observation-station-7/problem


--Solution

SELECT DISTINCT CITY 
FROM STATION 
WHERE substr(CITY, -1) IN ('a', 'e', 'i', 'o', 'u');
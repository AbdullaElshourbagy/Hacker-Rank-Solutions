--https://www.hackerrank.com/challenges/weather-observation-station-4/problem


--Solution

SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;
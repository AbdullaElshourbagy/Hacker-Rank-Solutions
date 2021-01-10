--https://www.hackerrank.com/challenges/weather-observation-station-10/problem



--Solution


SELECT DISTINCT CITY 
FROM STATION 
WHERE substr(CITY, -1) NOT IN ('a', 'e', 'i', 'o', 'u');
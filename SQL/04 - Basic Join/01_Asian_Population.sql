----https://www.hackerrank.com/challenges/asian-population/problem

--Solution

SELECT SUM(city.POPULATION)
FROM CITY city 
INNER JOIN COUNTRY 
ON CITY.COUNTRYCODE = COUNTRY.CODE 
WHERE COUNTRY.CONTINENT = 'Asia';
--https://www.hackerrank.com/challenges/african-cities/problem?h_r=next-challenge&h_v=zen

--Solution


SELECT city.NAME
FROM CITY city
INNER JOIN COUNTRY country
ON city.COUNTRYCODE = country.CODE 
WHERE country.CONTINENT = 'Africa';
--https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?h_r=next-challenge&h_v=zen


--Solution


SELECT country.CONTINENT, FLOOR(AVG(city.POPULATION))
FROM CITY city
INNER JOIN COUNTRY  country
ON city.COUNTRYCODE = country.CODE
GROUP BY country.CONTINENT;
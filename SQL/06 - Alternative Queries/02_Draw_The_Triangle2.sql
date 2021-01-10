---https://www.hackerrank.com/challenges/draw-the-triangle-2/problem

---Solution on MySql


SET @TEMP:=0; 
SELECT REPEAT('* ', @TEMP:= @TEMP + 1) 
FROM INFORMATION_SCHEMA.TABLES
WHERE @TEMP < 20;
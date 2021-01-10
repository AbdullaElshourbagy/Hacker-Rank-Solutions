--https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?h_r=next-challenge&h_v=zen


--Solution


SELECT W.ID, P.AGE, W.COINS_NEEDED, W.POWER 
FROM WANDS  W ,WANDS_PROPERTY  P
WHERE W.CODE = P.CODE AND P.IS_EVIL = 0 
AND W.COINS_NEEDED = (SELECT MIN(COINS_NEEDED) 
FROM WANDS  X, WANDS_PROPERTY  Y 
WHERE X.CODE = Y.CODE
AND  X.POWER = W.POWER AND Y.AGE = P.AGE) 
ORDER BY W.POWER DESC, P.AGE DESC;
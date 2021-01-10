#https://www.hackerrank.com/challenges/polar-coordinates/problem


#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar
z = complex(input())
tup= (polar(z))
print(tup[0])
print(tup[1])

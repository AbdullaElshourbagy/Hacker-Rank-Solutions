#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem


#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

String = input().split()
s,k = sorted(String[0]),int(String[1])
print(*list(map(''.join,combinations_with_replacement(s,k))),sep='\n')

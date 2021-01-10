#https://www.hackerrank.com/challenges/itertools-permutations/problem


#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

String = input().split()
s,k = sorted(String[0]),int(String[1])

print(*list(map(''.join,permutations(s,k))),sep='\n')

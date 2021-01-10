#https://www.hackerrank.com/challenges/itertools-combinations/problem



#Solution



# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

String = input().split()
s,k = sorted(String[0]),int(String[1])

for first_iter in range(1,int(k)+1):
    for second_iter in combinations(sorted(s), first_iter):
        print(''.join(second_iter))
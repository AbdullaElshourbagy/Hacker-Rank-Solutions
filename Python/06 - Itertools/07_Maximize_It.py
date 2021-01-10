#https://www.hackerrank.com/challenges/maximize-it/problem


#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
#define square method
def sqr(x):
    return x**2

K, M = map(int, input().split())
all_lists=[]
for i in range(K):
    lst = list(map(int, input().split()))
    del lst[0]
    all_lists.append(lst)
#make product for all alternatives 
products = list(product(*all_lists))
maxs = []
#calculate all alternatives
for i in products:
    res = sum(map(sqr, [a for a in i]))%M
    maxs.append(res)

print(max(maxs))
#https://www.hackerrank.com/challenges/iterables-and-iterators/problem

#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
word_lst = list(input().split())
K = int(input())

result_lst=list(combinations(word_lst,K))
contains_a=[s for s in result_lst if 'a' in s]
print(len(contains_a)/len(result_lst))

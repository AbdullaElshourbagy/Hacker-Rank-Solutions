#https://www.hackerrank.com/challenges/python-tuples/problem


#Solution


N = int(input())
print(hash(tuple(map(int, input().split()))))
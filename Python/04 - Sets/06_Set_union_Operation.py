#https://www.hackerrank.com/challenges/py-set-union/problem

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
n_students=set(map(int,input().split()))
b=int(input())
b_students=set(map(int,input().split()))
total=n_students.union(b_students)
print(len(total))

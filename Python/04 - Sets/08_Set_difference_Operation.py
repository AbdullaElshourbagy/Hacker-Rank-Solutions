#https://www.hackerrank.com/challenges/py-set-difference-operation/problem


#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
n_students=set(map(int,input().split()))
b=int(input())
b_students=set(map(int,input().split()))
total=n_students.difference(b_students)
print(len(total))


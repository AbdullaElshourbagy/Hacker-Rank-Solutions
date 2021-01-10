#https://www.hackerrank.com/challenges/py-check-subset/problem


#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())

for i in range(T):
   A=int(input())
   A_test_cases=set(map(int, input().split()))
   B=int(input())
   B_test_cases=set(map(int, input().split()))
   print(A_test_cases.issubset(B_test_cases))

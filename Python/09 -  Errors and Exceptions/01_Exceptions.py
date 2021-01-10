#https://www.hackerrank.com/challenges/exceptions/problem

#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except  ZeroDivisionError as e:
         print(f'Error Code: {e}')
    except ValueError as s:
        print(f'Error Code: {s}')
    

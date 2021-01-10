#https://www.hackerrank.com/challenges/incorrect-regex/problem



#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T= int(input())
for i in range(T):
    S=input()    
    try:
        res = re.compile(S)
        print("True")
    except Exception:
        print("False")
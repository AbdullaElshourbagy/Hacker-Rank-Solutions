#https://www.hackerrank.com/challenges/py-check-strict-superset/problem


#Solution

 # Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
st = set()
for i in range(n):
    bool_val = A > set(input().split())
    st.add(bool_val)
print(all(st))

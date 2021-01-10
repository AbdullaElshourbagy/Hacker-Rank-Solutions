#https://www.hackerrank.com/challenges/symmetric-difference/problem


#Solution



# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
M_set = set(map(int, input().split()))
N=int(input())
N_set = set(map(int, input().split()))
s=M_set.difference(N_set)
s.update(N_set.difference(M_set))
for i in sorted(s):
    print(i)





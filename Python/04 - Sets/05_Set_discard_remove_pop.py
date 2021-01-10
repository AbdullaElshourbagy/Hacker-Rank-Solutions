#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

#Solution

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    operations=input().split()
    if operations[0] =='pop':
        s.pop()
    elif operations[0] == 'remove':
        s.remove(int(operations[1]))
    elif operations[0] == 'discard':
        s.discard(int(operations[1]))

print(sum(s))


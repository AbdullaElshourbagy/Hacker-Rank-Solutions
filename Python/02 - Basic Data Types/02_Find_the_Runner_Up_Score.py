#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

#Solution


n = int(input())
arr = list(map(int, input().split()))
print(max([x for x in arr if x != max(arr)]))

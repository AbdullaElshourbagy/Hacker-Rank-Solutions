#https://www.hackerrank.com/challenges/string-validators/problem



#Solution

s = input()
print(any([i.isalnum() for i in s if i.isalnum()]))
print(any([i.isalpha() for i in s if i.isalpha()]))
print(any([i.isdigit() for i in s if i.isdigit()]))
print(any([i.islower() for i in s if i.islower()]))
print(any([i.isupper() for i in s if i.isupper()]))

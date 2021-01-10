#https://www.hackerrank.com/challenges/designer-door-mat/problem



#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
height, width = map(int, input().split())
for h in range(height // 2):
    print(('.|.' * (h * 2 + 1)).center(width,'-'))
print('WELCOME'.center(width, '-'))
for h in range(height // 2 - 1, -1, -1):
    print(('.|.' * (h * 2 + 1)).center(width,'-'))
	
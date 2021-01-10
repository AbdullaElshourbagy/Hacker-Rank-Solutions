#https://www.hackerrank.com/challenges/python-string-formatting/problem


#Solution


def print_formatted(number):
    # your code goes here
    space = len("{val:b}".format(val=number))
    for num in range(1,number+1):
        print("{num:{space}d} {num:{space}o} {num:{space}X} {num:{space}b}".format(num=num , space=space)) 
        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
	
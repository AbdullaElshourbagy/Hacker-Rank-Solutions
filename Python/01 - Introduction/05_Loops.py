#https://www.hackerrank.com/challenges/python-loops/problem

#Solution


if __name__ == '__main__':
    n = int(raw_input())
    if n>=1 and n<=20:
        for i in range(0 , n):
            print(i**2)

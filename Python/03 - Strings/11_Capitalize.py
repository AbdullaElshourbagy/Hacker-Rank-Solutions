#https://www.hackerrank.com/challenges/capitalize/problem



#Solution



import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(string):
    print(' '.join(word.capitalize() for word in string.split(' ')))

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

	
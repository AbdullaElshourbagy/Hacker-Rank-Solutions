#https://www.hackerrank.com/challenges/compress-the-string/problem


#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

for Key, list_occur in groupby(input()):
    print("(%d, %d)" % (len(list(list_occur)), int(Key)), end=' ')


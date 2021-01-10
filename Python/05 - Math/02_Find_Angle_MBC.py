#https://www.hackerrank.com/challenges/find-angle/problem


#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees, atan2
AB,BC=int(input()),int(input())
angel = round(degrees(atan2(AB, BC)))
print(str(angel) + '°')

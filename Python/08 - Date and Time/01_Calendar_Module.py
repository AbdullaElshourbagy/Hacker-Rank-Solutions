#https://www.hackerrank.com/challenges/calendar-module/problem

#Solution


# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

MM, DD, YY = map(int, input().split())

print(calendar.day_name[calendar.weekday(YY, MM, DD)].upper())


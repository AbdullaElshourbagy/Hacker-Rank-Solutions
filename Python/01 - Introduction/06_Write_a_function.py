#https://www.hackerrank.com/challenges/write-a-function/problem


#Solution


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year >= 1900 and year <= 10**5:
        if year % 4 ==0:
            leap = True 
            if year % 100 ==0:
                leap=False            
                if year % 400 ==0:
                   leap = True 

    return leap


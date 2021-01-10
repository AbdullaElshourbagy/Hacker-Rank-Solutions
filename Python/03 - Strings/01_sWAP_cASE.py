#https://www.hackerrank.com/challenges/swap-case/problem


#Solution




def swap_case(s):
    result=''
    for x in s:
        if x.islower():
            result=result+x.upper()
        else:
            result=result+x.lower()
    return result #s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
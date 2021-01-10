#https://www.hackerrank.com/challenges/find-a-string/problem


#Solution



def count_substring(string, sub_string):
    return len([i for i in range(len(string)) if string.startswith(sub_string, i)] )

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
	
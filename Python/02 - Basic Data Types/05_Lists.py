#https://www.hackerrank.com/challenges/python-lists/problem


#Solution


def perform_list_methods(lst):
    inserted_line = input().split()
    command=inserted_line[0]
    values=inserted_line[1:]
    if command=='print':
        print(lst)
    else:
        command='lst.'+command+'('+ ','.join(values) +')'
        eval(command)
        
        
        
N = int(input())
lst=[]
for iteration in range(N):
    perform_list_methods(lst)




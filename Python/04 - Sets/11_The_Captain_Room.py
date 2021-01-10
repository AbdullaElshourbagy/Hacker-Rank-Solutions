#https://www.hackerrank.com/challenges/py-the-captains-room/problem

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
K=int(input())
rooms_list=list(map(int,input().split()))
all_rooms=set()
temp_rooms=set()
for room in rooms_list:
    if room not in all_rooms:
        all_rooms.add(room)
        temp_rooms.add(room)
    else:
        temp_rooms.discard(room)
print(list(temp_rooms)[0])

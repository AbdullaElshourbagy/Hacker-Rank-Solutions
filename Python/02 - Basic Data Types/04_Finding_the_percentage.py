#https://www.hackerrank.com/challenges/finding-the-percentage/problem


#Solution



n = int(input())
student_marks = {}
for x in range(n):
    name, *line = input().split()
    scores = sum(list(map(float, line)))/3
   #scores= sum(line)/3
    student_marks[name] = scores
query_name = input()

print('%.2f' %  student_marks[query_name])

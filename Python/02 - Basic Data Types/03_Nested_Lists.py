#https://www.hackerrank.com/challenges/nested-list/problem


#Solution

def sort_scores(scores):
    result=sorted(set([x[1] for x in scores]))
    return result[1]

def get_names(value,scores):
    result=[x[0] for x in scores if x[1] == value]
    return sorted(result)

def print_names(names):
    for name in names:
        print(name)

scores=[]
for val in range(int(input())):
    name = input()
    score = float(input())
    scores.append([name,score])
#print(scores)

print_names(get_names(sort_scores(scores),scores))
    

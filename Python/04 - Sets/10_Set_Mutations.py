#https://www.hackerrank.com/challenges/py-set-mutations/problem


#Solution


def evaluate_set_operations(st):
    command = input().split()
    new_set = set(map(int, input().split()))
    if command[0] == 'update':
        st.update(new_set)
    elif command[0] == 'intersection_update':
        st.intersection_update(new_set)
    elif command[0] == 'difference_update':
        st.difference_update(new_set)
    elif command[0] == 'symmetric_difference_update':
        st.symmetric_difference_update(new_set)

a = input()
a_set = set(map(int, input().split()))
N = int(input())
for i in range(N):
    evaluate_set_operations(a_set)
print(sum(a_set))


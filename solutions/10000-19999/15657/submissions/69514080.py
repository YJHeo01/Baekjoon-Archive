from collections import deque

def backtracking(m,answer_list,num_list):
    if len(answer_list) == m:
        for i in answer_list:
            print(i,end=" ")
        print()
        return
    for i in list(num_list):
        answer_list.append(i)
        backtracking(m,answer_list,num_list)
        answer_list.pop()
    if num_list != deque([]):
        num_list.popleft()
    


n,m = map(int,input().split())

num_list = list(map(int,input().split()))

num_list.sort()

num_list = deque(num_list)

backtracking(m,[],num_list)
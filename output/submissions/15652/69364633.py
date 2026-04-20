def backtracking(l,answer_list,num_list):
    if len(answer_list) == l:
        for i in answer_list:
            print(i,end=" ")
        print()
        return
    for i in num_list:
        if i >= answer_list[-1]:
            answer_list.append(i)
            backtracking(l,answer_list,num_list)
            answer_list.pop()
    return

n,m = map(int,input().split())

num_list = [0]*n

for i in range(n):
    num_list[i] = i+1

for i in range(n):
    backtracking(m,[num_list[i]],num_list)
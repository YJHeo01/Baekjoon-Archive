n,m = map(int,input().split())

def backtracking(m,num_list,answer_list):
    if len(answer_list) == m:
        for i in range(m):
            print(answer_list[i],end=" ")
        print()
        return
    for n in num_list:
        if n not in answer_list:
            answer_list.append(n)
            backtracking(m,num_list,answer_list)
            answer_list.pop()

num_list = list(map(int,input().split()))

num_list.sort()

backtracking(m,num_list,[])
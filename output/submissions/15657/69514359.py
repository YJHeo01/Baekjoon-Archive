def backtracking(m,answer_list,num_list):
    if len(answer_list) == m:
        for i in answer_list:
            print(i,end=" ")
        print()
        return
    for i in num_list:
        if answer_list != [] and answer_list[0] > i:
            continue
        answer_list.append(i)
        backtracking(m,answer_list,num_list)
        answer_list.pop()


n, m = map(int,input().split())

num_list = list(map(int,input().split()))

num_list.sort()

backtracking(m,[],num_list)
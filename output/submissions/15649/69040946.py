def backtracking(m,answer_list,num_list):
    if len(answer_list) == m:
        for i in answer_list:
            print(i,end=" ")
        print()
        return
    for i in num_list:
        if i in answer_list:
            continue
        tmp = answer_list
        tmp.append(i)
        backtracking(m,tmp,num_list)
        tmp.pop()
    
    
n,m = map(int,input().split())

array = [1] * n

for i in range(1,n):
    array[i] = i+1
backtracking(m,[],array)
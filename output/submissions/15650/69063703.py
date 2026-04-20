answer = []

def backtracking(length,n_list,check_list):
    global answer
    if len(check_list) == length:
        l = len(num_list) + 1
        tmp = [0] * l
        for i in check_list:
            tmp[i] = 1
        if tmp not in answer:
            answer.append(tmp)

    for i in n_list:
        if i in check_list:
            continue
        check_list.append(i)
        backtracking(length,n_list,check_list)
        check_list.pop()
n,m = map(int,input().split())

num_list = [1] * (n)

for i in range(1,n):
    num_list[i] = i+1

backtracking(m,num_list,[])

for c in answer:
    for i in range(1,n+1):
        if c[i] == 1:
            print(i,end=" ")
    print()
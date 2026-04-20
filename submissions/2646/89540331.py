n = int(input())

array = sorted(list(map(int,input().split())))

min_value = array[n-1]

max_value = sum(array)

def backtracking(answer,tmp,visited,target,last_idx):
    cur_value = sum(tmp)
    if cur_value == target:
        answer.append(tmp)
        tmp = []
        cur_value = 0
        last_idx = -1
        finish = True
        for i in visited:
            if i == False: finish = False
        if finish:
            print(target)
            for row in answer:
                print(*row)
            exit(0)
        
    for i in range(last_idx+1,n):
        if visited[i]: continue
        if cur_value + array[i] > target: break
        visited[i] = True
        backtracking(answer,tmp+[array[i]],visited,target,i)
        visited[i] = False
    
    if cur_value == 0 and answer != []: answer.pop()

for i in range(min_value,max_value+1):
    backtracking([],[],[False]*n,i,-1)
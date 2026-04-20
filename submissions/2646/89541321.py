n = int(input())

array = sorted(list(map(int,input().split())))

min_value = array[n-1]

max_value = sum(array)

def backtracking(answer,tmp,visited,target,last_start,last_idx):
    cur_value = sum(tmp)
    start = last_idx + 1
    
    if cur_value == target:
        answer.append(tmp)
        if visited[last_idx] == n-1:
            print(target)
            for row in answer:
                print(*row)
            exit(0)
        tmp = []
        cur_value = 0
        start = last_start + 1
    
    for i in range(start,n):
        if visited[i] != -1: continue
        if cur_value + array[i] > target: break
        visited[i] = visited[last_idx] + 1
        tmp.append(array[i])
        if cur_value == 0:
            backtracking(answer,tmp,visited,target,i,i)
        else:
            backtracking(answer,tmp,visited,target,last_start,i)
        visited[i] = -1
        tmp.pop()
    
    if cur_value == 0 and answer != []: answer.pop()

for i in range(min_value,max_value+1):
    backtracking([],[],[-1]*n+[-1],i,-1,-1)
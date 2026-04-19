n = int(input())

array = sorted(list(map(int,input().split())))

min_value = array[n-1]

max_value = sum(array)

dp = [False] * (max_value+1)

dp[0] = True

for i in array:
    for j in range(max_value,-1,-1):
        if j + i > max_value or dp[j] == False: continue
        dp[j+i] = True

def backtracking(answer,tmp,visited,target,last_start,last_idx,cur_value):
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
        while True:
            if start == n:
                answer.pop()
                return
            if visited[start] == -1: break
            start += 1
        for i in range(start):
            if visited[i] == -1:
                answer.pop()
                return
    
    for i in range(start,n):
        if visited[i] != -1: continue
        if cur_value + array[i] > target: break
        if cur_value + array[i] != target and cur_value + array[i] * 2 > target: break
        visited[i] = visited[last_idx] + 1
        tmp.append(array[i])
        if cur_value == 0:
            backtracking(answer,tmp,visited,target,i,i,cur_value+array[i])
        else:
            backtracking(answer,tmp,visited,target,last_start,i,cur_value+array[i])
        visited[i] = -1
        tmp.pop()
    
    if cur_value == 0 and answer != []: answer.pop()

visited = [-1] * (n+1)

for i in range(min_value,max_value//2+1):
    if dp[i] == False or max_value % i != 0: continue
    backtracking([],[],visited,i,-1,-1,0)

print(max_value)
for i in array: print(i,end=" ")
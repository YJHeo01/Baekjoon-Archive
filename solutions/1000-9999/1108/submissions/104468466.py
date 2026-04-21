from collections import deque

n = int(input())

convert = dict()

cnt = 0

graph = [[] for _ in range(n+1500)]
matrix = [[0]*(n+1500) for _ in range(n+1500)]

for _ in range(n):
    tmp = list(input().split())
    start = tmp[0]
    if start not in convert:
        convert[start] = cnt
        cnt += 1
    b = convert[start]
    for end in tmp[2:]:
        if end not in convert:
            convert[end] = cnt
            cnt += 1
        a = convert[end]
        matrix[a][b] = 1
        graph[a].append(b)

indegree = [0] * cnt
score = [1] * cnt

for a in range(cnt):
    for b in graph[a]:
        if matrix[a][b] == matrix[b][a]:
            continue
        indegree[b] += 1

queue = deque([])

for i in range(cnt):
    if indegree[i] == 0:
        queue.append(i)

def dfs(graph,visited,x,target):
    ret_value = True
    visited[x] = True
    for nx in graph[x]:
        if visited[nx]: continue
        if nx == target: return False
        ret_value = dfs(graph,visited,nx,target)
        if ret_value == False: return ret_value
    visited[x] = False
    return ret_value

while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if matrix[nx][x] == 1: continue
        indegree[nx] -= 1
        if dfs(graph,[False]*cnt,nx,x): score[nx] += score[x]
        if indegree[nx] == 0:
            queue.append(nx)
            
target = input()
print(score[convert[target]])
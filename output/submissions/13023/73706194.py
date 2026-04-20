import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

graph = [[]for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,visited,start):
    if graph[start] == []:
        return 1
    visited[start] = True
    ret_value = 0
    for next_idx in graph[start]:
        if visited[next_idx] == True:
            continue
        ret_value = max(ret_value,dfs(graph,visited,next_idx))
        if ret_value >= 4:
            break
    visited[start] = False
    return ret_value + 1

answer = 0
for i in range(n):
    visited = [False] * n
    if dfs(graph,visited,i) >= 5:
        answer = 1
        break

print(answer)
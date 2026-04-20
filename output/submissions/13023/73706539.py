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
    if graph[start] == [] or visited[start] == 5:
        return 1
    ret_value = 0
    for next_idx in graph[start]:
        if visited[next_idx] != 0:
            continue
        visited[next_idx] = visited[start] + 1
        ret_value = max(ret_value,dfs(graph,visited,next_idx))
    visited[start] = 0
    return ret_value + 1

answer = 0
visited = [0] * n
for i in range(n):
    visited[i] = 1
    if dfs(graph,visited,i) >= 5:
        answer = 1
        break
    visited[i] = 0

print(answer)
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

taller_graph = [[]for _ in range(n+1)]
smaller_graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    taller_graph[a].append(b)
    smaller_graph[b].append(a)

answer = 0

def dfs(graph,visited,start):
    ret_value = 0
    if visited[start] == False:
        visited[start] = True
        ret_value += 1
    for nx in graph[start]:
        ret_value += dfs(graph,visited,nx)
    return ret_value

for i in range(1,n+1):
    visited = [False]*(n+1)
    visited_cnt = dfs(taller_graph,visited,i)
    visited_cnt += dfs(smaller_graph,visited,i)
    if visited_cnt == n:
        answer += 1

print(answer)
import sys

sys.setrecursionlimit(10**6+1)

t = int(input())

def dfs(graph,visited,start,vx):
    nx = graph[vx]
    if nx == start: return True
    if visited[nx] or nx < start: return False
    visited[nx] = True
    visited[nx] = dfs(graph,visited,start,nx)
    return visited[nx]

for _ in range(t):
    n = int(input())
    array = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    for i in range(1,n+1):
        if visited[i]: continue
        visited[i] = True
        visited[i] = dfs(array,visited,i,i)
    answer = 0
    for i in range(1,n+1):
        if visited[i] == False: answer += 1
    print(answer)
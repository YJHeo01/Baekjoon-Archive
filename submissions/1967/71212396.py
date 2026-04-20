import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(idx,cost,visited):
    visited[idx] = True
    ret_value = 0
    for i in graph[idx]:
        if visited[i[0]] == False:
            ret_value = max(ret_value,dfs(i[0],i[1],visited))
    return ret_value + cost

answer = 0

for i in range(1,n+1):
    answer = max(answer,dfs(i,0,[False]*(n+1)))
print(answer)
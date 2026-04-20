import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
target_node = [True] * (n+1)
target_node[0] = False
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    target_node[a] = False

def dfs(idx,cost,visited):
    visited[idx] = True
    ret_value = 0
    for i in graph[idx]:
        if visited[i[0]] == False:
            ret_value = max(ret_value,dfs(i[0],i[1],visited))
    return ret_value + cost

answer = 0

for i in range(1,n+1):
    if target_node[i] == True:
        answer = max(answer,dfs(i,0,[False]*(n+1)))
print(answer)
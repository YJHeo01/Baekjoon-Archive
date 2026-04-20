import sys
sys.setrecursionlimit(100000)

import sys

input = sys.stdin.readline

def dfs(graph,visited,start,v):
    global answer
    visited[start] = v
    for i in graph[start]:
        if visited[i[0]] == -1:
            dfs(graph,visited,i[0],v+i[1])
            visited[i[0]] = -1
    #visited[start] = -1
    answer = max(answer,v)


v = int(input())
graph = [[]for _ in range(v+1)]
answer = 0
for i in range(1,v+1):
    tmp = list(map(int,input().split()))
    j = 1
    while 1:
        if tmp[j] == -1:
            break
        graph[i].append((tmp[j],tmp[j+1]))
        j+=2
for i in range(1,v+1):
    visited = [-1]*(v+1)
    dfs(graph,visited,i,0)
print(answer)
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

indegree = [0]*(n+1)
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    indegree[b] += 1
    graph[a].append(b)

answer = 0
root_list = []

for i in range(n,0,-1):
    if indegree[i] == 0:
        answer += 1
        root_list.append(i)

def bfs(graph,visited,start):
    ret_value = 0
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        visited[vx] = True
        if graph[vx] == []:
            ret_value += 1
        for nx in graph[vx]:
            if visited[nx] == False:
                queue.append(nx)
visited = [False] * (n+1)

for root in root_list:
    bfs(graph,visited,root)

print(answer)
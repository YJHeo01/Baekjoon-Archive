from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[]for _ in range(n+1)]

start = [True] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    start[b] = False

def bfs(graph,visited,start):
    visited[start] = 1
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] < visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

answer_list = [0] * (n+1)
for i in range(1,n+1):
    if start[i] == True:
        bfs(graph,answer_list,i)

for answer in answer_list[1:]:
    print(answer,end=" ")
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

INF = int(1e9)

graph = [[]for _ in range(n+1)]

visited = [INF] * (n+1)

for _ in range(n-1):
    a,b= map(int,input().split())
    graph[a].append(b)

def bfs(graph,visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    
num_list = list(map(int,input().split()))

answer = 1

bfs(graph,visited)

for i in range(1,n):
    if visited[num_list[i-1]] > visited[num_list[i]]:
        answer = 0
        break

print(answer)
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
visited = [INF] * (n+1)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

bfs(graph,visited,1)

array = list(map(int,input().split()))

def solution(visited,array):
    for i in range(1,n):
        if visited[array[i-1]] > visited[array[i]]:
            return 0
    return 1

answer = solution(visited,array)

print(answer)
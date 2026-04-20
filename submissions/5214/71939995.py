import sys

input = sys.stdin.readline

from collections import deque

n,k,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    tmp = list(map(int,input().split()))
    for i in range(k):
        for j in range(i+1,k):
            graph[tmp[i]].append(tmp[j])
            graph[tmp[j]].append(tmp[i])

INF = int(1e9)

visited = [INF] * (n+1)

def bfs(graph,visited):
    queue = deque([1])
    visited[1] = 1
    while queue:
        station = queue.popleft()
        for next_station in graph[station]:
            if next_station == n:
                return visited[station] + 1
            if visited[next_station] > visited[station] + 1:
                visited[next_station] = visited[station] + 1
                queue.append(next_station)
    return -1

print(bfs(graph,visited))
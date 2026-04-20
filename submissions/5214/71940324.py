import sys

input = sys.stdin.readline

from collections import deque

n,k,m = map(int,input().split())

station_list = [[] for _ in range(n+1)]

hypertube = []
for i in range(m):
    tmp = list(map(int,input().split()))
    for j in tmp:
        station_list[j].append(i)
    hypertube.append(tmp)

INF = int(1e9)

visited = [INF] * (n+1)

def bfs(graph,visited):
    queue = deque([1])
    visited[1] = 1
    while queue:
        station = queue.popleft()
        for next_hypertube in graph[station]:
            for next_station in hypertube[next_hypertube]:
                if next_station == n:
                    return visited[station] + 1
                if visited[next_station] > visited[station] + 1:
                    visited[next_station] = visited[station] + 1
                    queue.append(next_station)
    return -1

print(bfs(station_list,visited))
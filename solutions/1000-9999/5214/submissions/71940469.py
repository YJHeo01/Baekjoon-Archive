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

visited_station = [INF] * (n+1)
visited_hypertube = [False] * m
def bfs(graph,visited_station,visited_hypertube):
    queue = deque([1])
    visited_station[1] = 1
    while queue:
        station = queue.popleft()
        for next_hypertube in graph[station]:
            if visited_hypertube[next_hypertube] == True:
                continue
            visited_hypertube[next_hypertube] = True
            for next_station in hypertube[next_hypertube]:
                if next_station == n:
                    return visited_station[station] + 1
                if visited_station[next_station] > visited_station[station] + 1:
                    visited_station[next_station] = visited_station[station] + 1
                    queue.append(next_station)
    return -1

print(bfs(station_list,visited_station,visited_hypertube))
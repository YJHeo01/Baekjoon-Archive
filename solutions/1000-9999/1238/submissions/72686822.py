import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
n,m,x = map(int,input().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, time = map(int,input().split())
    road[start].append((end,time))

home_x = [0] * (n+1)
x_home = [0] * (n+1)

def dijkstra_home_x(start):
    distance = [INF] * (n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in road[now]:
            if distance[i[0]] > distance[now] + i[1]:
                distance[i[0]] = distance[now] + i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))
    return distance[x]

def dijkstra_x_home(start):
    distance = [INF] * (n+1)
    q = []
    distance[x] = 0
    heapq.heappush(q,(0,x))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in road[now]:
            if distance[i[0]] > distance[now] + i[1]:
                distance[i[0]] = distance[now] + i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))
    return distance[start]

answer = 0
for i in range(1,n+1):
    home_x[i] = dijkstra_home_x(i)
    x_home[i] = dijkstra_x_home(i)
    answer = max(answer,home_x[i]+x_home[i])

print(answer)

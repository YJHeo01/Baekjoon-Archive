import sys, heapq

input = sys.stdin.readline

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    x,y,t,k = map(int,input().split())
    graph[x].append((y,t,k))
    graph[y].append((x,t,k))

INF = int(1e9)

answer = [INF] * (v+1)
distance = [INF] * (v+1)
max_taste = [0] * (v+1)

distance[1] = 0
answer[1] = 0

q = []

heapq.heappush(q,(0,0,0,1))

while q:
    value, dist, taste, x = heapq.heappop(q)
    if value > answer[x] and dist > distance[x] and max_taste[x] > taste: continue
    for nx,t,k in graph[x]:
        next_dist = dist + t
        next_taste = max(taste,k)
        next_value = next_dist - next_taste
        if answer[nx] > value or distance[nx] > next_dist or next_taste > max_taste[nx]:
            answer[nx] = min(answer[nx],next_value)
            distance[nx] = min(distance[nx],next_dist)
            max_taste[nx] = max(max_taste[nx],next_taste)
            heapq.heappush(q,(next_value,next_dist,next_taste,nx))

for i in range(2,v+1):
    print(answer[i])
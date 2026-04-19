import heapq,sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
road_list = []

for _ in range(m):
    a,b,time = map(int,input().split())
    road_list.append([a,b])
    graph[a].append((b,time))
    graph[b].append((a,time))


def dijkstra(graph,distance,block_road):
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if block_road[vx][nx] == True:
                continue
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))
distance = [INF] * (n+1) 
block_road = [[False]*(n+1) for _ in range(n+1)]
dijkstra(graph,distance,block_road)
orignal_time = distance[n]

last_road = [0,0]
answer = 0
for road in road_list:
    last_road_x,last_road_y = last_road
    block_road[last_road_x][last_road_y] = False
    block_road[last_road_y][last_road_x] = False
    last_road = road
    x,y = road
    block_road[x][y] = True
    block_road[y][x] = True
    distance = [INF] * (n+1)
    dijkstra(graph,distance,block_road)
    new_time = distance[n]
    if new_time >= INF:
        answer = -1
        break
    answer = max(answer,new_time-orignal_time)

print(answer)
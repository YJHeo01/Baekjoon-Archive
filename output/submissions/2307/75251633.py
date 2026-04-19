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

path = [0] * (n+1)

def get_original_time(graph,distance,path):
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                path[nx] = vx
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))
    return distance[n]
distance = [INF] * (n+1) 
block_road = [[False]*(n+1) for _ in range(n+1)]
orignal_time = get_original_time(graph,distance,path)
answer = 0
vx = n

def get_new_time(graph,distance,block_road):
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
    return distance[n]

while True:
    nx = path[vx]
    block_road[vx][nx] = True
    block_road[nx][vx] = True
    distance = [INF] * (n+1)
    new_time = get_new_time(graph,distance,block_road)
    if new_time >= INF:
        answer = -1
        break
    answer = max(answer,new_time-orignal_time)
    block_road[vx][nx] = False
    block_road[nx][vx] = False
    vx = nx
    if vx == 1:
        break

print(answer)
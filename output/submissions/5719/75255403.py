from collections import deque
import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def get_shortest_path(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
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

def get_block_road(graph,distance,block_road):
    queue = deque([d])
    while queue:
        vx = queue.popleft()
        for nx, length in graph[vx]:
            if block_road[nx][vx] == True:
                continue
            if distance[vx] == distance[nx] + length:
                block_road[nx][vx] = True
                queue.append(nx)

def solution(graph,distance,block_road):
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
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

while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    s,d = map(int,input().split())
    graph = [[] for _ in range(n)]
    graph_reverse = [[] for _ in range(n)]
    for _ in range(m):
        u,v,p = map(int,input().split())
        graph[u].append((v,p))
        graph_reverse[v].append((u,p))
    distance = [INF] * n
    block_road = [[False]*n for _ in range(n)]
    get_shortest_path(graph,distance,s)
    original_length = distance[d]
    get_block_road(graph_reverse,distance,block_road)
    distance = [INF] * n
    solution(graph,distance,block_road)
    answer = distance[d]
    if answer >= INF:
        answer = -1
    print(answer)

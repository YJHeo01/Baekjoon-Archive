import sys,heapq

input = sys.stdin.readline

n, robot1, robot2 = map(int,input().split())

graph = [[] for _ in range(n+1)]
tunnel = []

for _ in range(n-1):
    a,b,length = list(map(int,input().split()))
    graph[a].append((b,length))
    graph[b].append((a,length))
    tunnel.append((a,b))

INF = int(1e9)

robot1_to_room_distance = [INF] * (n+1)
robot2_to_room_distance = [INF] * (n+1)

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

dijkstra(graph,robot1_to_room_distance,robot1)
dijkstra(graph,robot2_to_room_distance,robot2)

answer = INF

for a,b in tunnel:
    answer = min(answer,robot1_to_room_distance[a]+robot2_to_room_distance[b],robot1_to_room_distance[b]+robot2_to_room_distance[a])

print(answer)
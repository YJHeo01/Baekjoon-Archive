import heapq

INF = int(1e9)

t = int(input())

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx,dx in graph[vx]:
            if distance[nx] > distance[vx] + dx:
                distance[nx] = distance[vx] + dx
                heapq.heappush(q,(distance[nx],nx))

for _ in range(t):
    n,m = map(int,input().split())
    graph = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    k = int(input())
    sum_distance_list = [0] * (n+1)
    friend_list = list(map(int,input().split()))
    for friend in friend_list:
        distance = [INF] * (n+1)
        dijkstra(graph,distance,friend)
        for i in range(n,0,-1):
            sum_distance_list[i] += distance[i]
    answer_idx = 0
    answer_distance = INF
    for i in range(n,0,-1):
        if answer_distance >= sum_distance_list[i]:
            answer_idx = i
            answer_distance = sum_distance_list[i]
    print(answer_idx)
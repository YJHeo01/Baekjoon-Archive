import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
adj_matrix = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    adj_matrix[a][b] = w
    adj_matrix[b][a] = w

def dijkstra(graph,distance,path,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx in graph[vx]:
            time = adj_matrix[vx][nx]
            if distance[nx] > dist + time:
                path[nx] = vx
                distance[nx] = dist + time
                heapq.heappush(q,(distance[nx],nx))

def search_first_visit_node(path,start,end):
    node = end
    while True:
        next_node = path[node]
        if next_node == start:
            return node
        else:
            node = next_node
for start in range(1,n+1):
    distance = [INF] * (n+1)
    path = [0] * (n+1)
    dijkstra(graph,distance,path,start)
    for end in range(1,n+1):
        if start == end:
            print('-',end=" ")
        else:
            answer = search_first_visit_node(path,start,end)
            print(answer,end=" ")
    print()
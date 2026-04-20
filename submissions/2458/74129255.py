import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

adj_matrix_A = [[INF]*(n+1)]
adj_matrix_B = [[INF]*(n+1)]

adj_graph_A = [[]for _ in range(n+1)]
adj_graph_B = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adj_graph_A[a].append(b)
    adj_graph_B[b].append(a)

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        vd, vx = heapq.heappop(q)
        if vd > distance[vx]:
            continue
        for nx in graph[vx]:
            if distance[nx] > vd + 1:
                distance[nx] = vd + 1
                heapq.heappush(q,(distance[nx],nx))

    
for i in range(1,n+1):
    distance_A = [INF] * (n+1)
    distance_B = [INF] * (n+1)
    dijkstra(adj_graph_A,distance_A,i)
    dijkstra(adj_graph_B,distance_B,i)
    adj_matrix_A.append(distance_A)
    adj_matrix_B.append(distance_B)

answer = n

for i in range(1,n+1):
    for j in range(1,n+1):
        if adj_matrix_A[i][j] >= INF and adj_matrix_B[i][j] >= INF:
            answer -= 1
            break
print(answer)
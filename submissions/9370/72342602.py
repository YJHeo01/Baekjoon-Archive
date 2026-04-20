import heapq
import sys

input = sys.stdin.readline

T = int(input())

INF = int(1e9)

def dijkstra(graph,distance_list,start):
    distance_list[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance_list[now]:
            continue
        for i in graph[now]:
            if distance_list[i[0]] > distance_list[now] + i[1]:
                distance_list[i[0]] = distance_list[now] + i[1]
                heapq.heappush(q,(i[1],i[0]))
    
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    dest_list = []
    start_mid_distance = [INF] * (n+1)
    for _ in range(t):
        dest_list.append(int(input()))
    dest_list.sort()
    start_dest_destination = [INF] * (n+1)
    dijkstra(graph,start_dest_destination,s)
    dijkstra(graph,start_mid_distance,s)
    if start_mid_distance[g] > start_mid_distance[h]:
        mid_idx = g
    else:
        mid_idx = h
    mid_dest_distance = [INF] * (n+1)
    dijkstra(graph,mid_dest_distance,mid_idx)
    for dest in dest_list:
        if start_mid_distance[mid_idx] + mid_dest_distance[dest] == start_dest_destination[dest]:
            print(dest,end=" ")
    print()
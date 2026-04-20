import sys, heapq

input = sys.stdin.readline

INF = int(1e9)

TC = int(input())


for _ in range(TC):
    answer = 'NO'
    n,m,w = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,t = map(int,input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))

    for _ in range(w):
        s,e,t = map(int,input().split())
        graph[s].append((e,-t))
    def dijkstra(start,distance):
        q = []
        distance[start] = 0
        heapq.heappush(q,(0,start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for v in graph[now]:
                if distance[v[0]] > distance[now] + v[1]:
                    distance[v[0]] = distance[now] + v[1]
                    heapq.heappush(q,(v[1],v[0]))
    for i in range(1,n+1):
        distance = [INF] * (n+1)
        dijkstra(i,distance)
        if distance[i] < 0:
            answer = 'YES'
            break
    print(answer)
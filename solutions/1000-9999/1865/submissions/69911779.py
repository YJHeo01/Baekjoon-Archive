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

    def solution(start,distance):
        q = []
        distance[start] = 0
        heapq.heappush(q,start)
        while q:
            now = heapq.heappop(q)
            for v in graph[now]:
                if distance[v[0]] > distance[now] + v[1]:
                    if v[0] == start and distance[now] + v[1] < 0:
                        return 1
                    distance[v[0]] = distance[now] + v[1]
                    heapq.heappush(q,v[0])
        return 0
    for i in range(1,n+1):
        distance = [INF] * (n+1)
        tmp = solution(i,distance)
        if tmp == 1:
            answer = 'YES'
            break
    print(answer)

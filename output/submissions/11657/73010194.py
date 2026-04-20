import sys,heapq

input = sys.stdin.readline

n,m= map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

INF = int(1e9)

def solution(graph):
    distance = [INF] * (n+1)
    distance[1] = 0
    q = []
    heapq.heappush(q,(0,1))
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            next_dist = dist + i[1]
            if distance[i[0]] > next_dist:
                if next_dist < 0:
                    return -1
                distance[i[0]] = next_dist
                heapq.heappush(q,(next_dist,i[0]))
    return distance

answer = solution(graph)

if answer == -1:
    print(-1)
else:
    for i in range(2,n+1):
        if answer[i] == INF:
            print(-1)
        else:
            print(answer[i])
import sys,heapq

input = sys.stdin.readline

n,m,t = map(int,input().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    u,v,h = map(int,input().split())
    graph[u].append((v,h))

INF = int(1e9)

max_high = [[INF]*(n+1) for _ in range(n+1)]

def solution(graph,max_high,start):
    q = []
    max_high[start][start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > max_high[start][now]:
            continue
        for next_node, next_hurdle in graph[now]:
            if max_high[start][next_node] > next_hurdle:
                max_high[start][next_node] = next_hurdle
                heapq.heappush(q,(next_hurdle,next_node))

for _ in range(t):
    s,e = map(int,input().split())
    if max_high[s][s] == INF:
        solution(graph,max_high,s)
    answer = max_high[s][e]
    if answer == INF:
        answer = -1
    print(answer)
import sys,heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start,end = map(int,input().split())

limit = [0] * (n+1)

INF = int(1e9)

def solution(graph,limit,start):
    q = []
    heapq.heappush(q,(-INF,start))
    limit[start] = INF
    while q:
        vx_limit, vx = heapq.heappop(q)
        vx_limit *= -1
        if limit[vx] > vx_limit:
            continue
        for nx, bridge_limit in graph[vx]:
            nx_limit = min(vx_limit,bridge_limit)
            if nx_limit > limit[nx]:
                limit[nx] = nx_limit
                heapq.heappush(q,(-nx_limit,nx))

solution(graph,limit,start)

answer = limit[end]

print(answer)
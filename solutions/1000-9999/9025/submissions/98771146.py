import sys, heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m,s,e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    for i in range(1,n+1):
        graph[a].sort(key= lambda x:(-x[1],x[0]))
        bandwidth = [0] * (n+1)
        INF = int(1e9)
        q = []
        heapq.heappush(q,(-INF,s))
        bandwidth[s] = INF
        while q:
            d, x = heapq.heappop(q)
            d *= -1
            if bandwidth[x] != d: continue
            for nx,dd in graph[x]:
                nd = min(dd,d)
                if bandwidth[nx] >= nd: continue
                bandwidth[nx] = nd
                heapq.heappush(q,(-nd,nx))
    print(bandwidth[e])
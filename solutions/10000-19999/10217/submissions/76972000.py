import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

t = int(input())

def solution(graph,cost_time):
    q = []
    heapq.heappush(q,(0,0,1))
    cost_time[1][0] = 0
    while q:
        vc, vt, vx = heapq.heappop(q)
        if vt > cost_time[vx][vc]:
            continue
        for nx, dc, dt in graph[vx]:
            nc = vc + dc
            if nc > m:
                continue
            nt = vt + dt
            if cost_time[nx][nc] > nt:
                cost_time[nx][nc] = nt
                heapq.heappush(q,(nc,nt,nx))
                for i in range(nc+1,m+1):
                    if cost_time[nx][i] > nt:
                        cost_time[nx][i] = nt
                    else:
                        break

for _ in range(t):
    n,m,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = map(int,input().split())
        graph[u].append((v,c,d))
    cost_time = [[INF]*(m+1) for _ in range(n+1)]
    solution(graph,cost_time)
    answer = min(cost_time[n])
    if answer >= INF:
        answer = "Poor KCM"
    print(answer)
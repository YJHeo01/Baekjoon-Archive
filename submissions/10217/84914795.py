import sys, heapq

input = sys.stdin.readline

def main():
    t = int(input())
    global m
    n,m,k = map(int,input().split())
    ticket = [[] for _ in range(n+1)]
    time = [[INF]*(m+1) for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = map(int,input().split())
        ticket[u].append((v,c,d))
    dijkstra(ticket,time)
    answer = min(time[n])
    if answer >= INF:
        print("Poor KCM")
    else:
        print(answer)

def dijkstra(graph,time):
    q = []
    time[1][0] = 0
    heapq.heappush(q,(0,0,1))
    while q:
        vt, vc, vx = heapq.heappop(q)
        if vt > time[vx][vc]:
            continue
        for nx, dc, dt in graph[vx]:
            nc = vc + dc
            nt = vt + dt
            if nc > m: continue
            if time[nx][nc] > nt:
                time[nx][nc] = nt
                heapq.heappush(q,(nt,nc,nx))

if __name__ == "__main__":
    INF = int(1e9)
    main()
import sys, heapq

input = sys.stdin.readline

def main():
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
    ret_value = INF
    while q:
        vt, vc, vx = heapq.heappop(q)
        if vt > min(time[vx][vc],ret_value):
            continue
        if vx == n:
            ret_value = min(ret_value,vt)
            continue
        for nx, dc, dt in graph[vx]:
            nc = vc + dc
            nt = vt + dt
            if nc > m: continue
            if time[nx][nc] > nt:
                time[nx][nc] = nt
                heapq.heappush(q,(nt,nc,nx))
    return ret_value

if __name__ == "__main__":
    INF = int(1e9)
    t = int(input())
    n,m,k = map(int,input().split())
    main()
import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    for _ in range(t):        
        graph = [[] for _ in range(n+1)]
        for _ in range(k):
            u,v,c,d = map(int,input().split())
            graph[u].append((v,c,d))
        time = [[INF] * (m+1) for _ in range(n+1)]
        max_cost = [0] * (n+1)
        min_cost = [m] * (n+1)
        dijkstra(graph,time,max_cost,min_cost)
        answer = min(time[n])
        if answer >= INF:
            print("Poor KCM")
        else:
            print(answer)

def dijkstra(graph,time,max_cost,min_cost):
    q = []
    time[1][0] = 0
    min_cost[1] = 0
    heapq.heappush(q,(0,0,1))
    while q:
        vt, vc, vx = heapq.heappop(q)
        if vt > time[vx][vc] or vc > max_cost[vx]  or vt > time[vx][min_cost[vx]] :
            continue
        for nx, dc, dt in graph[vx]:
            nc = vc + dc; nt = vt + dt
            if nc > m or time[nx][nc] <= nt:
                continue
            time[nx][nc] = nt        
            if min_cost[nx] > nc:
                min_cost[nx] = nc
                if max_cost[nx] == 0:
                    max_cost[nx] = nc
            else:
                if nt >= time[nx][min_cost[nx]]:
                    continue
                if time[nx][max_cost[nx]] >= nt:
                    if time[nx][max_cost[nx]] == nt and nc > max_cost[nx]:
                        continue
                    max_cost[nx] = nc
                if nc > max_cost[nx]:
                    continue 
                      
            heapq.heappush(q,(nt,nc,nx))

if __name__ == "__main__":
    t = int(input())
    n,m,k = map(int,input().split())
    main()
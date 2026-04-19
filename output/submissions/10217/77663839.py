import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    graph = get_graph()
    time = [[INF] * (m+1) for _ in range(n+1)]
    max_cost = [0] * (n+1)
    dijkstra(graph,time,max_cost)
    answer = min(time[n])
    if answer >= INF:
        print("Poor KCM")
    else:
        print(answer)
    
def get_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = map(int,input().split())
        graph[u].append((v,c,d))
    return graph

def dijkstra(graph,time,max_cost):
    q = []
    time[1][0] = 0
    heapq.heappush(q,(0,0,1))
    while q:
        vt, vc, vx = heapq.heappop(q)
        if vt > time[vx][vc] or vt > time[vx][max_cost[vx]]:
            continue
        for nx, dc, dt in graph[vx]:
            nc = vc + dc; nt = vt + dt
            if nc > m or time[nx][max_cost[nx]] < nt:
                continue
            if nc > max_cost[nx]:
                time[nx][nc] = nt
                max_cost[nx] = nc
                heapq.heappush(q,(nt,nc,nx))
            else:
                if time[nx][nc] > nt:
                    time[nx][nc] = nt
                    heapq.heappush(q,(nt,nc,nx))

if __name__ == "__main__":
    t = int(input())
    n,m,k = map(int,input().split())
    main()
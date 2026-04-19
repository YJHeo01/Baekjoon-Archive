import sys, heapq

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        global m
        n,m,k = map(int,input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(k):
            u,v,c,d = map(int,input().split())
            graph[u].append((c,d,v))
        for i in range(n+1):
            graph[i].sort()
        distance = [[INF]*(m+1) for _ in range(n+1)]
        dijkstra(graph,distance)
        answer = min(distance[n])
        if answer >= INF:
            print("Poor KCM")
        else:
            print(answer)

def dijkstra(graph,distance):
    q = []
    heapq.heappush(q,(0,0,1))
    while q:
        vc, vt, vx = heapq.heappop(q)
        if vt > distance[vx][vc]: continue
        for dc, dt, nx in graph[vx]:
            nc = vc + dc
            if nc > m: break
            nt = vt + dt
            if distance[nx][nc] > nt:
                distance[nx][nc] = nt
                heapq.heappush(q,(nc,nt,nx))

if __name__ == "__main__":
    INF = int(1e9)
    main()
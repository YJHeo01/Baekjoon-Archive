import sys,heapq

input = sys.stdin.readline

INF = 200000 * 100000 * 100

def main():
    high = [0] + list(map(int,input().split()))
    graph = get_graph(high)
    hp_start_to_target = [INF] * (n+1)
    hp_target_to_end = [INF] * (n+1)
    dijkstra(graph,hp_start_to_target,1)
    dijkstra(graph,hp_target_to_end,n)
    answer = -INF
    for i in range(2,n):
        answer = max(answer,high[i]*e-(hp_start_to_target[i]+hp_target_to_end[i])*d)
    if answer <= -INF:
        print("Impossible")
    else:
        print(answer)

def get_graph(high):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        if high[a] == high[b]: continue
        if high[a] > high[b]: a,b = b,a
        graph[a].append((b,c))
    return graph

def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        vd, vx = heapq.heappop(q)
        if vd > distance[vx]: continue
        for nx, length in graph[vx]:
            nd = vd + length
            if nd >= distance[nx]: continue
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))

if __name__ == "__main__":
    n,m,d,e = map(int,input().split())
    main()
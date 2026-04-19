import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = get_graph(n,m)
    x,z = map(int,input().split())
    answer = INF
    input()
    distance_XtoY = [INF] * (n+1)
    dijkstra(graph,distance_XtoY,x)
    if distance_XtoY[z] >= INF:
        print(-1)
        return
    y_list = list(map(int,input().split()))
    for y in y_list:
        if distance_XtoY[y] >= INF: continue
        distance_YtoZ = [INF] * (n+1)
        dijkstra(graph,distance_YtoZ,y)
        answer = min(answer,distance_XtoY[y]+distance_YtoZ[z])
        if answer == distance_XtoY[z]: break
    print(answer)

def get_graph(n,m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    return graph

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        vd, vx = heapq.heappop(q)
        if vd > distance[vx]: continue
        for nx, dd in graph[vx]:
            nd = vd + dd
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

if __name__ == "__main__":
    INF = int(1e9)
    main()
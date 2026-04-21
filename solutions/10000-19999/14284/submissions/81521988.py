import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    s,t = map(int,input().split())
    INF = int(1e9)
    distance = [INF] * (n+1)
    dijkstra(graph,distance,s)
    print(distance[t])
    
def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, dd in graph[vx]:
            nd = dist + dd
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

if __name__ == "__main__":
    main()
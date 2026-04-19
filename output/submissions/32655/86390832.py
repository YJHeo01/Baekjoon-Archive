import sys, heapq

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    x = int(input())
    e = list(map(int,input().split()))
    distance = [INF] * (n+1)
    answer = INF
    dijkstra(graph,distance,1)
    for i in range(x):
        target = e[i]
        tmp = (distance[target] // (k*x)) * k * x + i * k
        if distance[target] < tmp or distance[target] >= tmp + k:
            answer = min(answer,tmp - i * k +k*x)
        else:
            answer = min(answer,distance[target])
    print(answer)

def dijkstra(graph,distance,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, dd in graph[vx]:
            nd = dist + dd
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

if __name__ == "__main__":
    INF = int(1e18)
    main()
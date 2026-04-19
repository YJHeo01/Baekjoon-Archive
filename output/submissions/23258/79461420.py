import sys, heapq

input = sys.stdin.readline

def main():
    n,q = map(int,input().split())
    graph = get_graph(n)
    for _ in range(q):
        c,s,e = map(int,input().split())
        distance = [INF] * (n+1)
        dijkstra(graph,distance,s,c)
        answer = distance[e]
        if answer >= INF: answer = -1
        print(answer)

def get_graph(n):
    graph = [[] for _ in range(n+1)]
    for start in range(1,n+1):
        tmp = list(map(int,input().split()))
        for end in range(n):
            if tmp[end] == 0:continue
            graph[start].append((end+1,tmp[end]))
    return graph

def dijkstra(graph,distance,s,c):
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, time in graph[vx]:
            if distance[nx] > dist + time:
                distance[nx] = dist + time
                if nx >= c: continue
                heapq.heappush(q,(distance[nx],nx))

if __name__ == "__main__":
    INF = int(1e9)
    main() 
import sys, heapq

input = sys.stdin.readline

def main():
    n,m,x,y = map(int,input().split())
    adj_graph = [[] for _ in range(n)]
    _pq = [[] for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        adj_graph[a].append((b,c))
        adj_graph[b].append((a,c))
    for i in range(n):
        distance = [INF] * n
        dijkstra(adj_graph,distance,i)
        tmp = []
        for j in range(n):
            heapq.heappush(tmp,(distance[j],j))
        _pq[i] = tmp
    visited = [False] * n
    answer = 1
    while _pq[y]:
        dist, vx = heapq.heappop(_pq[y])
        if dist > x: break
        if visited[vx] == True: continue
        visited[vx] = True
        answer += 1
        while True:
            if _pq[vx] == []:
                break
            length, nx = heapq.heappop(_pq[vx])
            if visited[nx] == True: continue
            dist += length
            if dist > x:
                heapq.heappush(_pq[vx],(length,nx))
                break
            visited[nx] = True
            vx = nx
    for i in range(n):
        if visited[i] == False:
            answer = -1
            break
    print(answer)
            
def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))
    return distance

if __name__ == "__main__":
    INF = int(1e9)
    main()
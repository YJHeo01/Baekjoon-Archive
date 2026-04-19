import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    n,m = map(int,input().split())
    graph = get_graph(n,m)
    fox_shortest_path = [INF] * (n+1)
    fox_dijkstra(graph,fox_shortest_path)
    wolf_shortest_path = [[INF]*2 for _ in range(n+1)]
    wolf_dijkstra(graph,wolf_shortest_path)
    answer = 0
    for i in range(1,n+1):
        if fox_shortest_path[i] >= min(wolf_shortest_path[i]): continue
        answer += 1
    print(answer)

def get_graph(n,m):
    graph = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph

def fox_dijkstra(graph,distance):
    q = []
    distance[1] = 0
    heapq.heappush(q,(0,1))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, length in graph[vx]:
            nx_dist = dist + length
            if nx_dist >= distance[nx]: continue
            distance[nx] = nx_dist; heapq.heappush(q,(nx_dist,nx))

def wolf_dijkstra(graph,distance):
    q = []
    heapq.heappush(q,(0,1,0))
    distance[1][0] = 0
    while q:
        dist, vx, state = heapq.heappop(q)
        if dist > distance[vx][state]: continue
        for nx, length in graph[vx]:
            next_state = get_next_state(state)
            if state == 0: nx_dist = dist + length / 2
            else: nx_dist = dist + length * 2
            if nx_dist >= distance[nx][next_state]: continue
            distance[nx][next_state] = nx_dist
            heapq.heappush(q,(nx_dist,nx,next_state))

def get_next_state(state):
    if state == 0: return 1
    return 0

if __name__ == "__main__":
    main()
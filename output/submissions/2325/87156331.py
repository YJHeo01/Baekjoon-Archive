import sys, heapq

sys.setrecursionlimit(3000)
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y,z = map(int,input().split())
        graph[x].append((y,z))
        graph[y].append((x,z))
    distance = [INF] * (n+1)
    dijkstra(graph,distance)
    shortest_path_matrix = [[False]*(n+1) for _ in range(n+1)]
    set_shortest_path_matrix(graph,distance,n,shortest_path_matrix)
    shortest_path = []
    global shortest_path_cnt
    shortest_path_cnt = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if shortest_path_matrix[i][j] == True:
                shortest_path.append((i,j))
                shortest_path_cnt += 1
    answer_distance = [[INF]*shortest_path_cnt for  _ in range(n+1)]
    solution(graph,answer_distance,shortest_path)
    print(max(answer_distance[n]))

def dijkstra(graph,distance):
    q = []
    distance[1] = 0
    heapq.heappush(q,(0,1))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx, dd in graph[vx]:
            nd = dist + dd
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

def set_shortest_path_matrix(graph,distance,vx,shortest_path):
    if vx == 1: return
    for nx, dd in graph[vx]:
        if distance[nx] + dd == distance[vx]:
            shortest_path[nx][vx] = True
            set_shortest_path_matrix(graph,distance,nx,shortest_path)

def solution(graph,distance,shortest_path):
    q = []
    for i in range(shortest_path_cnt):
        distance[1][i] = 0
        heapq.heappush(q,(0,i,1))
    while q:
        vd, shortest_path_idx, vx = heapq.heappop(q)
        if vd > distance[vx][shortest_path_idx]: continue
        for nx,dd in graph[vx]:
            if (vx,nx) == shortest_path[shortest_path_idx] or (nx,vx) == shortest_path[shortest_path_idx]: continue
            nd = vd + dd
            if distance[nx][shortest_path_idx] > nd:
                distance[nx][shortest_path_idx] = nd
                heapq.heappush(q,(nd,shortest_path_idx,nx))
    
if __name__ == "__main__":
    INF = int(1e9)
    main()
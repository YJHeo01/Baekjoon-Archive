import sys, heapq

input = sys.stdin.readline

def main():
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    INF = int(1e9)
    distance = [[INF]*n for _ in range(n)]
    print(solution(graph,distance))

def solution(graph,distance):
    q = [(0,0,0)]
    distance[0][0] = 0
    dx = [0,1]
    dy = [1,0]
    while q:
        vd, vx, vy = heapq.heappop(q)
        if vd > distance[vx][vy]: continue
        for i in range(2):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx >= n or ny >= n: continue
            nd = vd
            if graph[nx][ny] >= graph[vx][vy]:
                nd += (graph[nx][ny]-graph[vx][vy] + 1)
            if distance[nx][ny] > nd:
                distance[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))
    return distance[n-1][n-1]


if __name__ == "__main__":
    n = int(input())
    main()
import sys, heapq

input = sys.stdin.readline

def main():
    adj_matrix = [list(map(int,input().split())) for _ in range(n)]
    distance = [[[INF]*3 for _ in range(n)] for _ in range(n)]
    dijkstra(adj_matrix,distance)
    answer = min(distance[n-1][n-1])
    print(answer)

def dijkstra(graph,distance):
    q = []
    heapq.heappush(q,(0,0,0,0))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        dist, cnt, vx, vy = heapq.heappop(q)
        if dist > distance[vx][vy][cnt]: continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            nx_dist = dist + t
            if cnt == 2: nx_dist += graph[nx][ny]
            n_cnt = cnt + 1; n_cnt %= 3
            if distance[nx][ny][n_cnt] > nx_dist:
                distance[nx][ny][n_cnt] = nx_dist
                heapq.heappush(q,(nx_dist,n_cnt,nx,ny))
        
if __name__ == "__main__":
    INF = float('INF')
    n,t = map(int,input().split())
    main()
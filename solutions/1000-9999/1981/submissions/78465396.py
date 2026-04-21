import heapq

def main():
    matrix = get_matrix()
    start_value = matrix[0][0]
    max_value_best = [[[201]*(200-start_value+1)for _ in range(n)]for _ in range(n)]
    min_value_best = [[[201]*(start_value+1) for _ in range(n)]for _ in range(n)]
    dijkstra(matrix,max_value_best,min_value_best)
    answer = 201
    for min_value in range(start_value+1):
        answer = min(answer,min_value + min_value_best[n-1][n-1][min_value])
    print(answer)

def get_matrix():
    matrix = []
    for _ in range(n): matrix.append(list(map(int,input().split())))
    return matrix

def dijkstra(graph,max_value_best,min_value_best):
    q = []
    heapq.heappush(q,(0,0,0,0))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    max_value_best[0][0][0] = 0
    min_value_best[0][0][0] = 0
    first_value = graph[0][0]
    while q:
        cur_max, cur_min, vx, vy = heapq.heappop(q)
        if cur_min > max_value_best[vx][vy][cur_max] or cur_max > min_value_best[vx][vy][cur_min]: continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >=n: continue
            next_max = max(cur_max,graph[nx][ny]- first_value)
            next_min = max(cur_min,first_value - graph[nx][ny])
            if next_min >= max_value_best[nx][ny][next_max] or next_max >= min_value_best[nx][ny][next_min]: continue
            max_value_best[nx][ny][next_max] = next_min
            min_value_best[nx][ny][next_min] = next_max
            heapq.heappush(q,(next_max,next_min,nx,ny))

if __name__ == "__main__":
    n = int(input())
    main()
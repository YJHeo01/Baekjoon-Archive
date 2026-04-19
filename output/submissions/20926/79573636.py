import sys, heapq

input = sys.stdin.readline

def main():
    maze = get_maze(h)
    start = get_start(maze)
    visited = [[INF]*w for _ in range(h)]
    answer = dijkstra(maze,visited,start)
    if answer >= INF: answer = -1
    print(answer)

def get_maze(h):
    maze = []
    for _ in range(h):
        maze.append(list(input()))
    return maze

def get_start(maze):
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 'T':
                maze[i][j] = '0'
                return (i,j)

def dijkstra(graph,distance,start):
    q = []
    distance[start[0]][start[1]] = 0
    heapq.heappush(q,(0,start[0],start[1]))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    answer = INF
    while q:
        dist, vx, vy = heapq.heappop(q)
        if dist > distance[vx][vy]:continue
        for i in range(4):
            nx,ny = vx,vy
            time = 0
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 'H':
                    break
                if graph[nx][ny] == 'R':
                    nx -= dx[i]
                    ny -= dy[i]
                    if distance[nx][ny] > dist + time:
                        distance[nx][ny] = dist + time
                        heapq.heappush(q,(distance[nx][ny],nx,ny))
                    break
                if graph[nx][ny] == 'E':
                    answer = min(answer,dist+time)
                    break
                time += int(graph[nx][ny])
    return answer

if __name__ == "__main__":
    INF = int(1e9)
    w,h = map(int,input().split())
    main()
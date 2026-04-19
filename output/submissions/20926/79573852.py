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
        tmp = list(input())
        for i in range(w):
            if tmp[i].isdigit() == True: tmp[i] = int(tmp[i])
        maze.append(tmp)
    return maze

def get_start(maze):
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 'T':
                maze[i][j] = 0
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
                nx += dx[i]; ny += dy[i]
                if exit_maze(nx,ny) or graph[nx][ny] == 'H':break
                if type(graph[nx][ny]) != int:
                    if graph[nx][ny] == 'E': answer = min(answer,dist+time)
                    else:
                        nx -= dx[i]
                        ny -= dy[i]
                        if distance[nx][ny] > dist + time:
                            distance[nx][ny] = dist + time
                            heapq.heappush(q,(distance[nx][ny],nx,ny))                        
                    break
                time += graph[nx][ny]
    return answer

def exit_maze(x,y):
    if x < 0 or y < 0 or x >= h or y >= w: return True
    return False

if __name__ == "__main__":
    INF = int(1e9)
    w,h = map(int,input().split())
    main()
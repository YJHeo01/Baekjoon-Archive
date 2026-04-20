from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [list(map(int,input().split())) for _ in range(n)]
    start = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                start.append((i,j))
    visited = [[0]*m for _ in range(n)]
    bfs(graph,visited,start)
    answer = [0] * 3
    for i in range(n):
        for j in range(m):
            if graph[i][j] <= 0: continue
            answer[graph[i][j]-1] += 1
    print(*answer)

def bfs(graph,visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        if graph[vx][vy] == 3: continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if (visited[nx][ny] == 0 and graph[nx][ny] == 0) or (visited[nx][ny] == visited[vx][vy] + 1 and graph[nx][ny] + graph[vx][vy] == 3):
                visited[nx][ny] = visited[vx][vy] + 1
                graph[nx][ny] += graph[vx][vy]
                queue.append((nx,ny))

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
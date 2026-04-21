from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = get_graph(n)
    start_x, start_y, end_x, end_y = map(int,input().split())
    time = [[INF]*m for _ in range(n)]
    direction = [[[False]*4 for _ in range(m)]for _ in range(n)]
    start = (start_x-1,start_y-1)
    bfs(graph,time,direction,start)
    answer = time[end_x-1][end_y-1]
    if answer >= INF: answer = -1
    print(answer)

def get_graph(n):
    graph = []
    for _ in range(n): graph.append(list(input()))
    return graph

def bfs(graph,visited,direction,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            if direction[vx][vy][(i+2)%4] == True:continue
            nx, ny = vx,vy
            for _ in range(k):
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == '#':break
                if visited[nx][ny] < visited[vx][vy] +1 : continue
                direction[nx][ny][i] = True
                if visited[nx][ny] == visited[vx][vy] + 1: continue
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    INF = int(1e9)
    main()
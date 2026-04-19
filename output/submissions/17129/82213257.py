from collections import deque
import sys

input = sys.stdin.readline

def main():
    island = [list(input().rstrip()) for _ in range(n)]
    visited = [[INF]*m for _ in range(n)]
    start = get_start(island)
    target = get_target(island)
    bfs(island,visited,start)
    answer = INF
    for x,y in target:
        answer = min(answer,visited[x][y])
    if answer >= INF:
        print("NIE")
        return
    print("TAK")
    print(answer)

def get_start(island):
    for i in range(n):
        for j in range(m):
            if island[i][j] == '2':
                return (i,j)

def get_target(island):
    ret_value = []
    for i in range(n):
        for j in range(m):
            if int(island[i][j]) >= 3:
                ret_value.append((i,j))
    return ret_value

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == '1':
                continue
            if visited[nx][ny] == INF:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main()
from collections import deque
import sys

input = sys.stdin.readline

def main():
    global n,m
    n,m,k = map(int,input().split())
    block = [[False]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        block[x][y] = True
    distance = [[-1]*m for _ in range(n)]
    bfs(block,distance)
    print(distance[n-1][m-1])

def bfs(block,visited):
    queue = deque([(0,0)])
    visited[0][0] = 0
    dx_dy = [[(-1,-1),(-1,0),(0,1),(1,0),(1,-1),(0,-1)],[(-1,0),(-1,1),(0,1),(1,1),(1,0),(0,-1)]]
    while queue:
        vx, vy = queue.popleft()
        for dx,dy in dx_dy[vx%2]:
            nx, ny = vx + dx, vy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or block[nx][ny] or visited[nx][ny] != -1: continue
            visited[nx][ny] = visited[vx][vy] + 1
            queue.append((nx,ny))

if __name__ == "__main__":
    main()
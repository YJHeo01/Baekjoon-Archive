from collections import deque
import sys

input = sys.stdin.readline

def main():
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[-1]*m for _ in range(n)]
    bfs(board,visited)
    print(visited[n-1][m-1])

def bfs(board,visited):
    queue = deque([(0,0)])
    visited[0][0] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx,ny = vx,vy
            for _ in range(board[vx][vy]):
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
    
if __name__ == "__main__":
    n,m = map(int,input().split())
    if n == 1 and m == 1:
        print(0)
        exit(0)
    main()
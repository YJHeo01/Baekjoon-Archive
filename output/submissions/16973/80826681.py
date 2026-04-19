from collections import deque
import sys

input = sys.stdin.readline

def main():
    global h,w
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    h,w,sr,sc,fr,fc = map(int,input().split())
    visited = [[-1]*m for _ in range(n)]
    init_board(board,h,w)
    sr -= 1; sc -= 1; fr -= 1; fc -= 1
    bfs(board,visited,(sr,sc))
    print(visited[fr][fc])

def init_board(board,h,w):
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                for dx in range(h):
                    nx = x - dx
                    if nx < 0: break
                    for dy in range(w):
                        ny = y - dy
                        if ny < 0: break
                        board[nx][ny] = -1

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
            if nx < 0 or ny < 0 or nx >= (n-h+1) or ny >= (m-w+1) or graph[nx][ny] != 0:
                continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    
if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
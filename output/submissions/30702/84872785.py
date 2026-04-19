from collections import deque

def main():
    A = [list(input()) for _ in range(n)]
    B = [list(input()) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    impossible = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]: continue
            impossible += bfs(A,B,visited,(i,j))
    if impossible:
        print("NO")
    else:
        print('YES')

def bfs(A,B,visited,start):
    queue = deque([start])
    x,y = start
    visited[x][y] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or A[nx][ny] != A[vx][vy]:
                continue
            if visited[nx][ny] == False:
                if B[nx][ny] == B[vx][vy]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                else:
                    return 1
    return 0

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
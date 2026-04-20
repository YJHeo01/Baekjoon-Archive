from collections import deque

def main():
    A = [list(input()) for _ in range(n)]
    B = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            visited = [[False]*m for _ in range(n)]
            bfs(A,B,visited,(i,j))
    answer = "YES"
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                answer = "NO"
    print(answer)

def bfs(A,B,visited,start):
    queue = deque([start])
    x,y = start
    visited[x][y] = True
    before_color = A[x][y]
    after_color = B[x][y]
    A[x][y] = after_color
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if A[nx][ny] == before_color and visited[nx][ny] == False:
                visited[nx][ny] = True
                A[nx][ny] = after_color
                queue.append((nx,ny))

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
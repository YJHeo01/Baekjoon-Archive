from collections import deque
import sys

input = sys.stdin.readline

def main():
    global n,m
    n,m,a,b,k = map(int,input().split())
    block = [[False]*(m+1) for _ in range(n+1)]
    for _ in range(k):
        x,y = map(int,input().split())
        block[x][y] = True
    visited = [[-1]*(m+1) for _ in range(n+1)]
    start = list(map(int,input().split()))
    end_x,end_y = map(int,input().split())
    bfs(block,visited,start,a,b)
    print(visited[end_x][end_y])

def bfs(graph,visited,start,a,b):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0:continue
            blocking = False
            for ddx in range(a):
                for ddy in range(b):
                    nnx = nx + ddx
                    nny = ny + ddy
                    if nnx > n or nny > m or graph[nnx][nny]:
                        blocking = True
                        break
                if blocking == True:break
            if graph[nx][ny] or blocking: continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    
if __name__ == "__main__":
    main()
from collections import deque
import sys

input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        global h,w
        h,w = map(int,input().split())
        ground = [list(input().rstrip()) for _ in range(h)]
        visited = [[False]*w for _ in range(h)]
        answer = 0
        for i in range(h):
            for j in range(w):
                if ground[i][j] == '#' and visited[i][j] == False:
                    answer += 1
                    bfs(ground,visited,(i,j))
        print(answer)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if visited[nx][ny] == False and graph[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx,ny))

if __name__ == "__main__":
    main()
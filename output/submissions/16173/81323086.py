from collections import deque

def main():
    area = []
    for _ in range(n):
        area.append(list(map(int,input().split())))
    visited = [[False]*n for _ in range(n)]
    bfs(area,visited)
    if visited[n-1][n-1] == True:
        print("HaruHaru")
    else:
        print("Hing")

def bfs(graph,visited):
    queue = deque([(0,0)])
    while queue:
        vx,vy = queue.popleft()
        if graph[vx][vy] == -1: break
        dx = [0,graph[vx][vy]]
        dy = [graph[vx][vy],0]
        for i in range(2):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx >= n or ny >= n or visited[nx][ny] == True: continue
            visited[nx][ny] = True
            queue.append((nx,ny))

if __name__ == "__main__":
    n = int(input())
    main()
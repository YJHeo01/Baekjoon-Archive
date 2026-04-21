from collections import deque

def main():
    graph_A = [list(input()) for _ in range(n)]
    graph_B = [list(input()) for _ in range(n)]
    visited_A = [[False]*m for _ in range(n)]
    visited_B = [[False]*m for _ in range(n)]
    answer = "YES"
    for i in range(n):
        for j in range(m):
            if graph_A[i][j] == graph_B[i][j]:
                continue
            if visited_A[i][j] != visited_B[i][j]:
                answer = "NO"
            bfs(graph_A,visited_A,(i,j))
            bfs(graph_B,visited_B,(i,j))
    print(answer)

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = True
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == False and graph[nx][ny] == graph[vx][vy]:
                visited[nx][ny] = True
                queue.append((nx,ny))
            
if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
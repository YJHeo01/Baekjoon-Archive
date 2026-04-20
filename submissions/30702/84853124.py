from collections import deque

def main():
    graph_A = [list(input()) for _ in range(n)]
    graph_B = [list(input()) for _ in range(n)]
    visited_A = [[-1]*m for _ in range(n)]
    visited_B = [[-1]*m for _ in range(n)]
    answer = "YES"
    A_idx,B_idx = 0,0
    for i in range(n):
        for j in range(m):
            if visited_A[i][j] == -1:
                bfs(graph_A,visited_A,(i,j),A_idx)
                A_idx += 1
            if visited_B[i][j] == -1:
                bfs(graph_B,visited_B,(i,j),B_idx)
                B_idx += 1
    for i in range(n):
        for j in range(m):
            if visited_A[i][j] != visited_B[i][j]:
                answer = "NO"
    print(answer)

def bfs(graph,visited,start,idx):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = idx
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == False and graph[nx][ny] == graph[vx][vy]:
                visited[nx][ny] = idx
                queue.append((nx,ny))
            
if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
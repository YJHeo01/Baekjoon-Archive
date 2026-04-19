from collections import deque

def main():
    array = [list(map(int,input().split())) for _ in range(n)]
    password_candidate = [0] * (n*m+1)
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0: continue
            visited = [[-1]*m for _ in range(n)]
            solution(array,visited,password_candidate,(i,j))
    while password_candidate:
        answer = password_candidate.pop()
        if answer != 0:
            print(answer)
            return
    print(0)

def solution(graph,visited,answer,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        answer[visited[vx][vy]] = max(answer[visited[vx][vy]],graph[start[0]][start[1]]+graph[vx][vy])
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0: continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
from collections import deque

n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(input()))

visited = [[-1]*m for _ in range(n)]

def solution(graph,visited):
    ret_value = 0
    visited[0][0] = 0
    queue = deque([(0,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        vx, vy = int(vx), int(vy)
        for i in range(4):
            nx = vx + int(graph[vx][vy]) * dx[i]
            ny = vy + int(graph[vx][vy]) * dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 'H':
                continue
            if visited[nx][ny] != -1:
                return -1
            visited[nx][ny] = visited[vx][vy] + 1
            ret_value = max(ret_value,visited[nx][ny])
            queue.append((nx,ny))

    return ret_value + 1

print(solution(board,visited))
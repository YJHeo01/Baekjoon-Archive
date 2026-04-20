from collections import deque

n,k = map(int,input().split())

board = []

for _ in range(2):
    board.append(list(input()))

INF = int(1e9)

visited = [[INF]*n for _ in range(2)]
def solution(graph,visited):
    visited[0][0] = 0
    queue = deque([(0,0)])
    while queue:
        vx,vy = queue.popleft()
        if vx == 0:
            nx = 1
        else:
            nx = 0
        ny = vy + k
        if ny >= n:
            return 1
        else:
            if graph[nx][ny] == '1' and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
        for dy in [1,-1]:
            nx = vx
            ny = vy + dy
            if ny < 0:
                continue
            elif ny >= n:
                return 1
            else:
                if graph[nx][ny] == '1' and (ny >= visited[vx][vy]+1) and (visited[nx][ny] > visited[vx][vy] + 1):
                    visited[nx][ny] = visited[vx][vy] + 1
                    queue.append((nx,ny))
    return 0

answer = solution(board,visited)

print(answer)
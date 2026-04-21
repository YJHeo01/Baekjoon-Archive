from collections import deque

n = int(input())

board = []

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1
answer = 0

queue = deque([(0,0)])

for _ in range(n):
    board.append(list(map(int,input().split())))

dx = [0,1]
dy = [1,0]

while queue:
    vx, vy = queue.popleft()
    for i in range(2):
        nx = vx + dx[i] * board[vx][vy]
        ny = vy + dy[i] * board[vx][vy]
        if nx >= n or ny >= n:
            continue
        if board[nx][ny] == 0:
            answer += 1
        else:
            if visited[nx][ny] == 0:
                queue.append((nx,ny))
            visited[nx][ny] += visited[vx][vy]
    visited[vx][vy] = 0
print(answer)
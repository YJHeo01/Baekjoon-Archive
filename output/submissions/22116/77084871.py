from collections import deque

INF = int(1e9)

n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

distance = [[INF]*n for _ in range(n)]

def solution(graph,distance):
    queue = deque([(0,0)])
    distance[0][0] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            nd = max(distance[vx][vy],abs(graph[nx][ny]-graph[vx][vy]))
            if distance[nx][ny] > nd:
                distance[nx][ny] = nd
                queue.append((nx,ny))

solution(board,distance)

answer = distance[n-1][n-1]

print(answer)
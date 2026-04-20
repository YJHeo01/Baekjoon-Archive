#https://github.com/YJHeo01
#https://www.acmicpc.net/problem/1890

from collections import deque

n = int(input())

game_board = []

for _ in range(n):
    game_board.append(list(map(int,input().split())))

n -= 1

def bfs(graph):
    answer = 0
    queue = deque([(0,0)])
    dx = [0,1]
    dy = [1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(2):
            nx = vx + dx[i] * graph[vx][vy]
            ny = vy + dy[i] * graph[vx][vy]
            if nx < 0 or ny < 0 or nx > n or ny > n:
                continue
            if nx == n and ny == n:
                answer += 1
            else:
                if graph[nx][ny] != 0:
                    queue.append((nx,ny))
    return answer

answer = bfs(game_board)

print(answer)
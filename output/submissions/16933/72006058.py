from collections import deque
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

INF = int(1e9)

visited = [[[[INF]*m for _ in range(n)]for _ in range(k+1)]for _ in range(2)]

def search_next_time(c):
    if c == 0:
        return 1
    else:
        return 0


def bfs(graph,visited,k):
    queue = deque([(0,k,0,0)])
    visited[0][k][0][0] = 1
    dx = [0,0,1,0,-1]
    dy = [0,1,0,-1,0]
    while queue:
        time, crash_cnt, vx, vy = queue.popleft()
        for i in range(5):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny <0 or nx >= n or ny>=m:
                continue
            next_time = search_next_time(time)
            if graph[nx][ny] == '0':
                if visited[next_time][crash_cnt][nx][ny] > visited[time][crash_cnt][vx][vy] + 1:
                    visited[next_time][crash_cnt][nx][ny] = visited[time][crash_cnt][vx][vy] + 1
                    queue.append((next_time,crash_cnt,nx,ny))
            else:
                if time == 0 and crash_cnt > 0 and visited[next_time][crash_cnt-1][nx][ny] > visited[time][crash_cnt][vx][vy] + 1:
                    visited[next_time][crash_cnt-1][nx][ny] = visited[time][crash_cnt][vx][vy] + 1
                    queue.append((next_time,crash_cnt-1,nx,ny))
    answer = INF
    for i in range(2):
        for j in range(k+1):
            answer = min(answer,visited[i][j][n-1][m-1])
    if answer == INF:
        answer = -1
    return answer

print(bfs(matrix,visited,k))
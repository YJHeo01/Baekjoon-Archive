from collections import deque
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

def bfs(graph,visited):
    queue = deque([(k,0,0)])
    visited[k][0][0] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        crash_cnt, vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == '0':
                if visited[crash_cnt][nx][ny] > visited[crash_cnt][vx][vy] + 1:
                    visited[crash_cnt][nx][ny] = visited[crash_cnt][vx][vy] + 1
                    queue.append((crash_cnt,nx,ny))
            else:
                if crash_cnt > 0 and visited[crash_cnt-1][nx][ny] > visited[crash_cnt][vx][vy] + 1 + (visited[crash_cnt][vx][vy] % 2):
                    visited[crash_cnt-1][nx][ny] = visited[crash_cnt][vx][vy] + 1 + (visited[crash_cnt][vx][vy] % 2)
                    queue.append((crash_cnt-1,nx,ny))

INF = int(1e9)
visited = [[[INF]*m for _ in range(n)]for _ in range(k+1)]
bfs(matrix,visited)
def get_answer(visited):
    ret_value = INF
    for i in range(k,-1,-1):
        ret_value = min(ret_value, visited[i][n-1][m-1])
    ret_value += 1
    if ret_value >= INF:
        ret_value = -1
    return ret_value

answer = get_answer(visited)

print(answer)
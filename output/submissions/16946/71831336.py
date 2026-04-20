from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

visited = [[False]*m for _ in range(n)]
answer = [[0]*m for _ in range(n)]
def bfs(graph,visited,start,answer):
    plus_value = 1
    queue = deque([start])
    block_list = []
    visited[start[0]][start[1]] = True
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                if graph[nx][ny] == '1':
                    block_list.append((nx,ny))
                else:
                    plus_value += 1
                    queue.append((nx,ny))
    for block in block_list:
        answer[block[0]][block[1]] += plus_value
        visited[block[0]][block[1]] = False
    return


for i in range(n):
    for j in range(m):
        if matrix[i][j] == '0' and visited[i][j] == False:
            bfs(matrix,visited,(i,j),answer)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '1':
            print(answer[i][j]+1,end="")
        else:
            print("0",end="")
    print()
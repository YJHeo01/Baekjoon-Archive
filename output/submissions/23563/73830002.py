from collections import deque
import sys

input = sys.stdin.readline

h,w = map(int,input().split())

board = []

start = (-1,-1)
end = (-1,-1)

for i in range(h):
    tmp = list(input())
    board.append(tmp)
    for j in range(w):
        if tmp[j] == 'S':
            start = (i,j)
        elif tmp[j] == 'E':
            end = (i,j)
        else:
            continue

def check_adj_block(graph,point):
    x,y = point
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if graph[nx][ny] == '#':
            return True
    return False
def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '#':
                continue
            if check_adj_block(graph,(vx,vy)) == True and check_adj_block(graph,(nx,ny)) == True:
                time = 0
            else:
                time = 1
            if visited[nx][ny] > visited[vx][vy] + time:
                visited[nx][ny] = visited[vx][vy] + time
                queue.append((nx,ny))

INF= int(1e9)

visited = [[INF]*w for _ in range(h)]

bfs(board,visited,start)
print(visited[end[0]][end[1]])
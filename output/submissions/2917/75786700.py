import sys

input = sys.stdin.readline

from collections import deque

INF = int(1e9)

n,m = map(int,input().split())

forest = []

for _ in range(n):
    forest.append(list(input()))


tree = []

start = (-1,-1)
end = (-1,-1)
for i in range(n):
    for j in range(m):
        if forest[i][j] == '+':
            tree.append((i,j))
        elif forest[i][j] == 'V':
            start = (i,j)
        elif forest[i][j] == 'J':
            end = (i,j)
        else:
            continue

def get_tree_distance(visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
tree_distance = [[INF]*m for _ in range(n)]

get_tree_distance(tree_distance,tree)

visited = [[-1]*m for _ in range(n)]

def solution(tree_distance,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = tree_distance[start[0]][start[1]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny< 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] < min(visited[vx][vy],tree_distance[nx][ny]):
                visited[nx][ny] = min(visited[vx][vy],tree_distance[nx][ny])
                queue.append((nx,ny))

solution(tree_distance,visited,start)

answer = visited[end[0]][end[1]]

print(answer)
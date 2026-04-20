from collections import deque

INF = int(1e9)

n,m = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

forest = []

for _ in range(n):
    forest.append(list(input()))

start = (-1,-1)
flower = (-1,-1)

for i in range(n):
    for j in range(m):
        if forest[i][j] == 'S':
            start = (i,j)
        elif forest[i][j] == 'F':
            flower = (i,j)
        elif forest[i][j] == 'g':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or y < 0 or x >= n or y >= m:
                    continue
                if forest[x][y] == '.':
                    forest[x][y] = '#'

visited_Trash = [[INF]*m for _ in range(n)]
visited_side_Trash = [[INF]*m for _ in range(n)]

def solution(graph,visited_Trash,visited_side_Trash,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited_side_Trash[start[0]][start[1]] = 0
    visited_Trash[start[0]][start[1]] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            next_trash = 0
            next_trash_side = 0
            if graph[nx][ny] == 'g':
                next_trash = 1
            elif graph[nx][ny] == '#':
                next_trash_side = 1

            if visited_Trash[nx][ny] > visited_Trash[vx][vy] + next_trash:
                visited_Trash[nx][ny] = visited_Trash[vx][vy] + next_trash
                visited_side_Trash[nx][ny] = visited_side_Trash[vx][vy] + next_trash_side
                queue.append((nx,ny))
            elif (visited_Trash[nx][ny] == visited_Trash[vx][vy] + next_trash) and visited_side_Trash[nx][ny] > visited_side_Trash[vx][vy] + next_trash_side:
                visited_side_Trash[nx][ny] = visited_side_Trash[vx][vy] + next_trash_side
                queue.append((nx,ny))
            else:
                continue

solution(forest,visited_Trash,visited_side_Trash,start)

print(visited_Trash[flower[0]][flower[1]],visited_side_Trash[flower[0]][flower[1]])
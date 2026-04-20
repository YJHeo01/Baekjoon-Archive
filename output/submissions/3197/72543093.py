from collections import deque
import sys

input = sys.stdin.readline

lake = []

swan1,swan2 = (-1,-1),(-1,-1)

r,c = map(int,input().split())

water = [[False]*c for _ in range(r)]
swan_can_move = [[False]*c for _ in range(r)]

next_melt = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def search_water_next_to_ice(graph,visited,start):
    ret_value = []
    x,y = start
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >=c:
            continue
        if graph[nx][ny] == 'X':
            ret_value.append((nx,ny))
        else:
            visited[nx][ny] = True
    return ret_value

for i in range(r):
    tmp = list(input())
    lake.append(tmp)
    for j in range(c):
        if swan2 != (-1,-1):
            continue
        if tmp[j] == 'L':
            if swan1 == (-1,-1):
                swan1 = [(i,j)]
            else:
                swan2 = (i,j)

for i in range(r):
    for j in range(c):
        if lake[i][j] == '.' and water[i][j] == False:
            water[i][j] = True
            next_melt += search_water_next_to_ice(lake,water,(i,j))

def swan_move(graph,visited,start):
    ret_value = []
    queue = deque(start)
    for x,y in start:
        visited[x][y] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >=c:
                continue
            if graph[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
            else:
                ret_value.append((nx,ny))
    return ret_value

def melt_ice(graph,ice):
    for x,y in ice:
        graph[x][y] = '.'
    return

answer = 0

while True:
    melt_ice(lake,next_melt)
    tmp = []
    for start in next_melt:
        tmp += search_water_next_to_ice(lake,water,start)
    next_melt = tmp
    swan1 = swan_move(lake,swan_can_move,swan1)
    print(answer)
    if swan_can_move[swan2[0]][swan2[1]] == True:
        break
    answer += 1


print(answer-1)
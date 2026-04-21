import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)

n = int(input())

tile = []
tile_idx = 0
tile_idx_list = [[0]*n for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        length = n
    else:
        length = n - 1
    tmp = []
    for j in range(length):
        tile_idx += 1
        tmp.append(list(map(int,input().split())))
        tile_idx_list[i][j] = tile_idx
    tile.append(tmp)

distance = [[INF]*n for _ in range(n)]
last_visit_tile = [[0]*n for _ in range(n)]

def bfs(graph,distance,last_visit_tile):
    queue = deque([(0,0)])
    distance[0][0] = 1
    while queue:
        vx,vy = queue.popleft()
        if vx % 2 == 0:
            dx = [-1,0,1,-1,0,1]
            dy = [-1,-1,-1,0,1,0]
        else:
            dx = [-1,0,1,-1,0,1]
            dy = [0,-1,0,1,1,1]
        vp = 0; np = 1
        for i in range(6):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or tile_idx_list[nx][ny] == 0:
                continue
            if i >= 3:
                vp = 1; np = 0
            if graph[vx][vy][vp] == graph[nx][ny][np] and distance[nx][ny] > distance[vx][vy] + 1:
                distance[nx][ny] = distance[vx][vy] + 1
                last_visit_tile[nx][ny] = (vx,vy)
                queue.append((nx,ny))

def search_dest(distance):
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if distance[i][j] >= INF:
                continue
            return (i,j)

bfs(tile,distance,last_visit_tile)       
dest = search_dest(distance)

print(distance[dest[0]][dest[1]])

def search_shortest_path(last_visit_tile,tile_idx_list,dest):
    ret_value = []
    cur_tile = dest
    while True:
        cur_tile_x, cur_tile_y = cur_tile
        cur_tile_idx = tile_idx_list[cur_tile_x][cur_tile_y]
        ret_value.append(cur_tile_idx)
        if cur_tile_idx == 1:
            break
        cur_tile = last_visit_tile[cur_tile_x][cur_tile_y]
    ret_value.reverse()
    return ret_value

shortest_path = search_shortest_path(last_visit_tile,tile_idx_list,dest)
for answer in shortest_path:
    print(answer,end=" ")
from itertools import permutations
from collections import deque

board = []
INF = int(1e9)
data = [0,1,2,3,4]

test_case_list = list(permutations(data,5))

for _ in range(5):
    tmp = []
    for _ in range(5):
        tmp.append(list(map(int,input().split())))
    board.append(tmp)

start_end = [[0,0,4,4],[4,4,0,0],[0,4,4,0],[4,0,0,4]]
cube_curve_list = []

for i in range(4):
    for j in range(4):
        for k in range(4):
            cube_curve_list.append([0,i,j,k])

def convert_x_y(x,y):
    nx = 4-y
    ny = x
    return (nx,ny)

answer = INF

def bfs(graph,visited,cube_curve,start):
    queue = deque([[0]+start])
    dx = [-1,1]
    dy = [1,-1,0,0]
    dz = [0,0,1,-1]
    visited[0][start[0]][start[1]] = 0
    while queue:
        vx,vy,vz = queue.popleft()
        for i in range(4):
            nx = vx
            ny = vy + dy[i]
            nz = vz + dz[i]
            if ny < 0 or nz < 0 or ny >= 5 or nz >= 5 or graph[nx][ny][nz] == 0:
                continue
            if visited[nx][ny][nz] > visited[vx][vy][vz] + 1:
                visited[nx][ny][nz] = visited[vx][vy][vz] + 1
                queue.append([nx,ny,nz])
        for i in range(2):
            nx = vx + dx[i]
            ny = vy; nz = vz
            if nx < 0 or nx >= 5:
                continue
            covert_cnt = (cube_curve[nx] - cube_curve[vx]) % 4
            for _ in range(covert_cnt):
                ny, nz = convert_x_y(ny,nz)
            if graph[nx][ny][nz] == 1 and visited[nx][ny][nz] > visited[vx][vy][vz] + 1:
                visited[nx][ny][nz] = visited[vx][vy][vz] + 1
                queue.append([nx,ny,nz])
            
def get_answer(cube,start,end,bottom_curve):
    ret_value = INF
    for cube_curve in cube_curve_list:
        visited = [[[INF]*5 for _ in range(5)]for _ in range(5)]
        bfs(cube,visited,cube_curve+[bottom_curve],start)
        ret_value = min(ret_value,visited[4][end[0]][end[1]])
    return ret_value

for test_case in test_case_list:
    cube = []
    for idx in test_case:
        cube.append(board[idx])
    for start_x,start_y,end_x,end_y in start_end:
        if cube[0][start_x][start_y] == 0:
            continue
        target_x, target_y = end_x, end_y
        for curve in range(4):
            if cube[4][target_x][target_y] == 1:
                answer = min(answer,get_answer(cube,[start_x,start_y],(target_x,target_y),curve))
            target_x, target_y = convert_x_y(target_x,target_y)
    if answer == 12:
        break

if answer >= INF:
    answer = -1

print(answer)
from itertools import permutations
from collections import deque

INF = int(1e9)

def main():
    board = get_board()
    data = [0,1,2,3,4]
    test_case_list = list(permutations(data,5))
    start_end = [[0,0,4,4],[4,4,0,0],[0,4,4,0],[4,0,0,4]]
    answer = INF
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
                target_x, target_y = turn_right(target_x,target_y)
        if answer == 12:
            break
    if answer >= INF:
        answer = -1
    print(answer)

def get_board():
    board = []
    for _ in range(5):
        tmp = []
        for _ in range(5):
            tmp.append(list(map(int,input().split())))
        board.append(tmp)
    return board

def get_answer(cube,start,end,bottom_curve):
    ret_value = INF
    cube_curve_list = get_cube_curve_list()
    for cube_curve in cube_curve_list:
        visited = [[[INF]*5 for _ in range(5)]for _ in range(5)]
        bfs(cube,visited,cube_curve+[bottom_curve],start)
        ret_value = min(ret_value,visited[4][end[0]][end[1]])
    return ret_value

def get_cube_curve_list():
    cube_curve_list = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                cube_curve_list.append([0,i,j,k])
    return cube_curve_list

def bfs(graph,visited,cube_curve,start):
    queue = deque([[0]+start])
    visited[0][start[0]][start[1]] = 0
    while queue:
        vx,vy,vz = queue.popleft()
        queue += move_y_or_z(graph,visited,(vx,vy,vz))
        queue += move_x(graph,visited,cube_curve,(vx,vy,vz))

def move_y_or_z(graph,visited,start):
    ret_value = []
    vx,vy,vz = start
    dy = [1,-1,0,0]
    dz = [0,0,1,-1]
    for i in range(4):
        nx = vx
        ny = vy + dy[i]
        nz = vz + dz[i]
        if ny < 0 or nz < 0 or ny >= 5 or nz >= 5 or graph[nx][ny][nz] == 0:
            continue
        if visited[nx][ny][nz] > visited[vx][vy][vz] + 1:
            visited[nx][ny][nz] = visited[vx][vy][vz] + 1
            ret_value.append([nx,ny,nz])
    return ret_value

def move_x(graph,visited,cube_curve,start):
    vx,vy,vz = start
    dx = [-1,1]
    ret_value = []
    for i in range(2):
        nx = vx + dx[i]
        ny = vy; nz = vz
        if nx < 0 or nx >= 5:
            continue
        convert_cnt = (cube_curve[nx] - cube_curve[vx]) % 4
        for _ in range(convert_cnt):
            ny, nz = turn_right(ny,nz)
        if graph[nx][ny][nz] == 1 and visited[nx][ny][nz] > visited[vx][vy][vz] + 1:
            visited[nx][ny][nz] = visited[vx][vy][vz] + 1
            ret_value.append([nx,ny,nz])
    return ret_value

def turn_right(x,y):
    nx = 4-y
    ny = x
    return (nx,ny)

if __name__ == "__main__":
    main()
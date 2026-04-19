sea = []
shark = [0,0,0]

fish_position_direction = [[0,0,0] for _ in range(17)]

for i in range(4):
    fish_information = list(map(int,input().split()))
    tmp = []
    for j in range(4):
        fish_idx = fish_information[2*j]
        fish_direction = fish_information[2*j+1]
        fish_position_direction[fish_idx] = [i,j,fish_direction]
        tmp.append(fish_idx)
    sea.append(tmp)

first_dead_fish_idx = sea[0][0]
shark[2] = fish_position_direction[first_dead_fish_idx][2]
sea[0][0] = -1
fish_position_direction[first_dead_fish_idx][2] = 0

def get_next_direction(sea,position,cur_d):
    dx = [0,-1,-1,0,1,1,1,0,-1]
    dy = [0,0,-1,-1,-1,0,1,1,1]
    x,y = position
    for i in range(9):
        next_d = (cur_d+i) % 9
        if next_d == 0:
            continue
        nx = x + dx[next_d]
        ny = y + dy[next_d]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or sea[nx][ny] == -1:
            continue
        return next_d
    return 0

def move_fish(sea,fish_position_direction):
    dx = [0,-1,-1,0,1,1,1,0,-1]
    dy = [0,0,-1,-1,-1,0,1,1,1]
    for idx in range(1,17):
        if fish_position_direction[idx][2] == 0:
            continue
        cur_x, cur_y, cur_d = fish_position_direction[idx]
        next_d = get_next_direction(sea,(cur_x,cur_y),cur_d)
        if next_d == 0:
            continue
        next_x = cur_x + dx[next_d]
        next_y = cur_y + dy[next_d]
        if sea[next_x][next_y] == 0:
            sea[cur_x][cur_y] = 0
        else:
            other_fish_idx = sea[next_x][next_y]
            fish_position_direction[other_fish_idx][0] = cur_x
            fish_position_direction[other_fish_idx][1] = cur_y
            sea[cur_x][cur_y] = other_fish_idx
        fish_position_direction[idx] = [next_x,next_y,next_d]
        sea[next_x][next_y] = idx
    return 0

def get_new_sea(sea):
    new_sea = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_sea[i][j] = sea[i][j]
    return new_sea

def get_new_fish_position_direction(fish_position_direction):
    ret_value = [[0]*3 for _ in range(17)]
    for i in range(1,17):
        for j in range(3):
            ret_value[i][j] = fish_position_direction[i][j]
    return ret_value

def move_shark(sea,fish_position_direction,shark):
    ret_value = 0
    dx = [0,-1,-1,0,1,1,1,0,-1]
    dy = [0,0,-1,-1,-1,0,1,1,1]
    shark_x, shark_y, shark_d = shark
    sea[shark_x][shark_y] = 0
    nx = shark_x;ny = shark_y
    while True:
        nx += dx[shark_d]
        ny += dy[shark_d]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            break
        if sea[nx][ny] == 0:
            continue
        new_sea = get_new_sea(sea)
        new_fish_position_direction = get_new_fish_position_direction(fish_position_direction)
        dead_fish_idx = sea[nx][ny]
        new_shark_d = fish_position_direction[dead_fish_idx][2]
        new_fish_position_direction[dead_fish_idx][2] = 0
        new_sea[nx][ny] = -1
        ret_value = max(ret_value,dead_fish_idx+solution(new_sea,new_fish_position_direction,[nx,ny,new_shark_d]))
    return ret_value
        
def solution(sea,fish_position_direction,shark):
    ret_value = 0
    move_fish(sea,fish_position_direction)
    ret_value = move_shark(sea,fish_position_direction,shark)
    return ret_value

answer = first_dead_fish_idx + solution(sea,fish_position_direction,shark)

print(answer)
r,c,t = map(int,input().split())

room = []

for _ in range(r):
    room.append(list(map(int,input().split())))

air_cleaner = [(-1,-1),(-1,-1)]

for i in range(r):
    if room[i][0] == -1:
        air_cleaner = [(i,0),(i+1,0)]
        break

def check_move_dust(room,next_dust,position):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = position
    dust_size = room[x][y] // 5
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or room[nx][ny] == -1:
            continue
        next_dust[nx][ny] += dust_size
        room[x][y] -= dust_size

def north_wind(room,start,end):
    start_x, start_y = start
    end_x, end_y = end
    for i in range(start_x,end_x,-1):
        room[i][start_y], room[i-1][end_y] = room[i-1][end_y], room[i][start_y]

def east_wind(room,start,end):
    start_x, start_y = start
    end_x, end_y = end
    for i in range(start_y,end_y):
        room[start_x][i], room[end_x][i+1] = room[end_x][i+1], room[start_x][i]

def south_wind(room,start,end):
    start_x, start_y = start
    end_x, end_y = end
    for i in range(start_x,end_x):
        room[i][start_y], room[i+1][end_y] = room[i+1][end_y], room[i][start_y]

def west_wind(room,start,end):
    start_x, start_y = start
    end_x, end_y = end
    for i in range(start_y,end_y,-1):
        room[start_x][i], room[end_x][i-1] = room[end_x][i-1], room[start_x][i]

def high_air_cleaner(room,position):
    x,y = position
    north_wind(room,(x-1,y),(0,y))
    east_wind(room,(0,0),(0,c-1))
    south_wind(room,(0,c-1),(x,c-1))
    west_wind(room,(x,c-1),(x,1))
    room[x][y+1] = 0

def low_air_cleaner(room,position):
    x,y = position
    south_wind(room,(x+1,y),(r-1,y))
    east_wind(room,(r-1,0),(r-1,c-1))
    north_wind(room,(r-1,c-1),(x,c-1))
    west_wind(room,(x,c-1),(x,y+1))
    room[x][y+1] = 0

while True:
    if t == 0:
        break
    t -= 1
    move_dust = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] <= 0:
                continue
            check_move_dust(room,move_dust,(i,j))
    for i in range(r):
        for j in range(c):
            room[i][j] += move_dust[i][j]
    
    high_air_cleaner(room,air_cleaner[0])
    low_air_cleaner(room,air_cleaner[1])

answer = 2

for i in range(r):
    for j in range(c):
        answer += room[i][j]

print(answer)
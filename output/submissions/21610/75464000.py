n,m = map(int,input().split())

ground = []

for _ in range(n):
    ground.append(list(map(int,input().split())))

command_list = []

for _ in range(m):
    command_list.append(list(map(int,input().split())))

cloud_list = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

def move_cloud(cloud_list,command):
    dx = [0,0,-1,-1,-1,0,1,1,1]
    dy = [0,-1,-1,0,1,1,1,0,-1]
    d,s = command
    for cloud in cloud_list:
        cloud[0] += dx[d] * s
        cloud[1] += dy[d] * s
        cloud[0] %= n
        cloud[1] %= n

def rain(ground,cloud_list):
    for cloud in cloud_list:
        x,y = cloud
        ground[x][y] += 1

def erase_cloud_area(cloud_area,cloud_list):
    for cloud in cloud_list:
        x,y = cloud
        cloud_area[x][y] = True

def magic(ground,cloud_list):
    dx = [1,1,-1,-1]
    dy = [-1,1,-1,1]
    new_water = [[0]*n for _ in range(n)]
    for cloud in cloud_list:
        x,y = cloud
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if ground[nx][ny] != 0:
                new_water[x][y] += 1
    for cloud in cloud_list:
        x,y = cloud
        ground[x][y] += new_water[x][y]
    
def creative_new_cloud(ground,cloud_area):
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if cloud_area[i][j] == True:
                continue
            if ground[i][j] >= 2:
                ground[i][j] -= 2
                new_cloud.append([i,j])
    return new_cloud

for command in command_list:
    move_cloud(cloud_list,command)
    rain(ground,cloud_list)
    cloud_area = [[False]*n for _ in range(n)]
    erase_cloud_area(cloud_area,cloud_list)
    magic(ground,cloud_list)
    cloud_list = creative_new_cloud(ground,cloud_area)

answer = 0

for i in range(n):
    for j in range(n):
        answer += ground[i][j]

print(answer)
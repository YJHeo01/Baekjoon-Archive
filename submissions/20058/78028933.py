from collections import deque

def main():
    ground = get_ground()
    command = list(map(int,input().split()))
    for c in command:
        divide_ice(ground,[0,length],[0,length],n-c)
        melt_ice = [[False]*length for _ in range(length)]
        check_melt_ice(ground,melt_ice)
        start_melt_ice(ground,melt_ice)
    visited = [[False]*length for _ in range(length)]
    sum_ice_value, max_lump_size = get_answer(ground,visited)
    print(sum_ice_value)
    print(max_lump_size)

def get_ground():
    ground = []
    for _ in range(length):
        ground.append(list(map(int,input().split())))
    return ground

def divide_ice(ground,x,y,c):
    if c == 0:
        turn_ice(ground,x,y)
        return
    c -= 1; x1,x2 = x; y1,y2 = y
    mid_x = (x1+x2) // 2
    mid_y = (y1+y2) // 2
    divide_ice(ground,[x1,mid_x],[y1,mid_y],c)
    divide_ice(ground,[x1,mid_x],[mid_y,y2],c)
    divide_ice(ground,[mid_x,x2],[y1,mid_y],c)
    divide_ice(ground,[mid_x,x2],[mid_y,y2],c)

def turn_ice(ground,x,y):
    x1,x2 = x; y1,y2 = y
    new_ground = [[0]*(y2-y1) for _ in range(x2-x1)]
    max_x = x2 - 1
    length = x2 - x1
    for i in range(x1,x2):
        for j in range(y1,y2):
            new_ground[j-y1][max_x-i] = ground[i][j]
    for i in range(length):
        for j in range(length):
            ground[x1+i][y1+j] = new_ground[i][j]
    return

def check_melt_ice(ground,melt_ice):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for x in range(length):
        for y in range(length):
            if ground[x][y] <= 0: continue
            adj_ice_cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if exit_graph(nx,ny): continue
                if ground[nx][ny] > 0: adj_ice_cnt += 1
            if adj_ice_cnt < 3: melt_ice[x][y] = True

def exit_graph(x,y):
    if x < 0 or y < 0 or x >= length or y >= length:
        return True
    return False

def start_melt_ice(ground,melt_ice):
    for i in range(length):
        for j in range(length):
            if melt_ice[i][j] == True:
                ground[i][j] -= 1

def get_answer(ground,visited):
    sum_ice_value, max_lump_size = 0, 0 
    for i in range(length):
        for j in range(length):
            if ground[i][j] != 0:
                sum_ice_value += ground[i][j]
                if visited[i][j] == False:
                    max_lump_size = max(max_lump_size,get_lump_size(ground,visited,(i,j)))
    return sum_ice_value, max_lump_size

def get_lump_size(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]]  = True
    ret_value = 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_graph(nx,ny): continue
            if visited[nx][ny] == False and graph[nx][ny] > 0:
                ret_value += 1; visited[nx][ny] = True
                queue.append((nx,ny))
    return ret_value

if __name__ == "__main__":
    n,q = map(int,input().split())
    length = 2 ** n
    main()
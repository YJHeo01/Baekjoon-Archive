from collections import deque

def main():
    board = []
    line_up = get_line_up(board)
    answer = 0
    start_direction_list = [0,1,2]
    for i in range(1,n**2):
        start_x, start_y = line_up[i]
        end_x, end_y = line_up[i+1]
        visited = [[[INF]*3 for _ in range(n)]for _ in range(n)]
        start = []
        for d in start_direction_list:
            visited[start_x][start_y][d] = 0
            start.append([start_x,start_y,d])
        move_object(visited,start)
        start_direction_list = [0]
        tmp = visited[end_x][end_y][0]
        for j in range(1,3):
            if tmp > visited[end_x][end_y][j]:
                tmp = visited[end_x][end_y][j]
                start_direction_list = [j]
            elif tmp == visited[end_x][end_y][j]:
                start_direction_list.append(j)
        answer += tmp
    print(answer)

def get_line_up(board):
    ret_value = [[] for _ in range(n**2+1)]
    for i in range(n):
        tmp = list(map(int,input().split()))
        board.append(tmp)
        for j in range(n):
            ret_value[tmp[j]] = [i,j]
    return ret_value

def move_object(visited,start):
    queue = deque(start)
    while queue:
        vx,vy,vd = queue.popleft()
        if vd == 2:
            queue += move_knight(visited,(vx,vy))
        elif vd == 1:
            queue += move_bishop(visited,(vx,vy))
        else:
            queue += move_look(visited,(vx,vy))
        for i in range(1,3):
            nd = (vd + i) % 3
            if visited[vx][vy][nd] > visited[vx][vy][vd] + 1:
                visited[vx][vy][nd] = visited[vx][vy][vd] + 1
                queue.append([vx,vy,nd])

def move_knight(visited,start):
    ret_value = []
    dx = [1,1,2,2,-1,-1,-2,-2]
    dy = [-2,2,1,-1,2,-2,1,-1]
    vx,vy = start
    for i in range(8):
        nx = vx + dx[i]
        ny = vy + dy[i]
        if exit_board(nx,ny) or visited[nx][ny][2] <= visited[vx][vy][2] + 1: continue
        visited[nx][ny][2] = visited[vx][vy][2] + 1
        ret_value.append([nx,ny,2])
    return ret_value

def move_bishop(visited,start):
    ret_value = []
    vx,vy = start
    dx = [1,1,-1,-1]
    dy = [-1,1,-1,1]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        while True:
            if exit_board(nx,ny): break
            if visited[nx][ny][1] > visited[vx][vy][1] + 1:
                visited[nx][ny][1] = visited[vx][vy][1] + 1
                ret_value.append([nx,ny,1])
            nx += dx[i]; ny += dy[i]
    return ret_value

def move_look(visited,start):
    ret_value = []
    vx,vy = start
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = vx + dx[i]
        ny = vy + dy[i]
        while True:
            if exit_board(nx,ny): break
            if visited[nx][ny][0] > visited[vx][vy][0] + 1:
                visited[nx][ny][0] = visited[vx][vy][0] + 1
                ret_value.append([nx,ny,0])
            nx += dx[i]; ny += dy[i]
    return ret_value

def exit_board(x,y):
    if x < 0 or y < 0 or x >= n or y >= n: return True
    return False

if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    main()
n,m = map(int,input().split())

board = []

Blue = (-1,-1)
Red = (-1,-1)

for i in range(n):
    tmp = list(input())
    board.append(tmp)
    if Blue == (-1,-1) or Red == (-1,-1):
        for j in range(m):
            if tmp[j] == 'B':
                Blue = [i,j]
                board[i][j] = '.'
            elif tmp[j] == 'R':
                Red = [i,j]
                board[i][j] = '.'
            else:
                continue

def direction(move_type):
    if move_type == 'L':
        return (0,-1)
    elif move_type == 'R':
        return (0,1)
    elif move_type == 'N':
        return (-1,0)
    else:
        return (1,0)
    
def move_ball(graph,move_type,start):
    x,y = start
    dx,dy = direction(move_type)
    while True:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >=m or graph[nx][ny] == '#':
            break
        elif graph[nx][ny] == 'O':
            return [nx,ny]
        else:
            x,y = nx,ny
    return [x,y]
INF = int(1e9)

def move_north(graph,Red,Blue):
    if Red[0] < Blue[0]:
        Red = move_ball(graph,'N',Red)
        Blue = move_ball(graph,'N',Blue)
        if Red == Blue and graph[Blue[0]][Blue[1]] != 'O':
            Blue[0] += 1
    else:
        Blue = move_ball(graph,'N',Blue)
        Red = move_ball(graph,'N',Red)
        if Red == Blue:
            Red[0] += 1
    return Red,Blue

def move_south(graph,Red,Blue):
    if Red[0] > Blue[0]:
        Red = move_ball(graph,'S',Red)
        Blue = move_ball(graph,'S',Blue)
        if Red == Blue and graph[Blue[0]][Blue[1]] != 'O':
            Blue[0] -= 1
    else:
        Blue = move_ball(graph,'S',Blue)
        Red = move_ball(graph,'S',Red)
        if Red == Blue:
            Red[0] -= 1
    return Red,Blue

def move_left(graph,Red,Blue):
    if Red[1] < Blue[1]:
        Red = move_ball(graph,'L',Red)
        Blue = move_ball(graph,'L',Blue)
        if Red == Blue and graph[Blue[0]][Blue[1]] != 'O':
            Blue[1] += 1
    else:
        Blue = move_ball(graph,'L',Blue)
        Red = move_ball(graph,'L',Red)
        if Red == Blue:
            Red[1] += 1
    return Red,Blue

def move_right(graph,Red,Blue):
    if Red[1] > Blue[1]:
        Red = move_ball(graph,'R',Red)
        Blue = move_ball(graph,'R',Blue)
        if Red == Blue and graph[Blue[0]][Blue[1]] != 'O':
            Blue[1] -= 1
    else:
        Blue = move_ball(graph,'R',Blue)
        Red = move_ball(graph,'R',Red)
        if Red == Blue:
            Red[1] -= 1
    return Red,Blue

def control(graph,Red,Blue,move_cnt):
    if graph[Blue[0]][Blue[1]] == 'O':
        return INF
    if graph[Red[0]][Red[1]] == 'O':
        return move_cnt
    if move_cnt > 10:
        return INF
    move_north_Red, move_north_Blue = move_north(graph,Red,Blue)
    move_south_Red, move_south_Blue = move_south(graph,Red,Blue)
    move_right_Red, move_right_Blue = move_right(graph,Red,Blue)
    move_left_Red, move_left_Blue = move_left(graph,Red,Blue)
    
    return min(control(graph,move_left_Red,move_left_Blue,move_cnt+1),control(graph,move_right_Red,move_right_Blue,),control(graph,move_south_Red,move_south_Blue,move_cnt+1),control(graph,move_north_Red,move_north_Blue,move_cnt+1))

answer = control(board,Red,Blue,0)

if answer == INF:
    answer = -1

print(answer)
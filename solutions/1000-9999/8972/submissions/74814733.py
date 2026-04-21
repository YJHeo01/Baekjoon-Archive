import sys

input = sys.stdin.readline

INF = int(1e9)

r,c = map(int,input().split())

board = []

crazy_arduino_list = []

jongsu = [-1,-1]
for _ in range(r):
    board.append(list(input())) # 보드 입력

for i in range(r):
    for j in range(c):
        if board[i][j] != '.':
            if board[i][j] == 'R':
                crazy_arduino_list.append([i,j])
            else:
                jongsu = [i,j]

command = list(input().rstrip())

def move_jongsu(board,jongsu,c):
    dx = [-1,1,1,1,0,0,0,-1,-1]
    dy = [1,-1,0,1,-1,0,1,-1,0]
    jongsu_x,jongsu_y = jongsu
    board[jongsu_x][jongsu_y] = '.'
    command = int(c) % 9
    jongsu[0] +=  dx[command]
    jongsu[1] +=  dy[command]
    jongsu_x, jongsu_y = jongsu
    board[jongsu_x][jongsu_y] = 'I'

def check_game_over(board,crazy_arduino_list,jongsu):
    remove_arduino_position = [[False]*c for _ in range(r)]
    exist_romove_arduino = False
    jongsu_x,jongsu_y = jongsu
    for crazy_arduino in crazy_arduino_list:
        if crazy_arduino[0] <= -1:
            continue
        board[crazy_arduino[0]][crazy_arduino[1]] = '.'
    for crazy_arduino in crazy_arduino_list:
        if crazy_arduino[0] <= -1:
            continue
        if crazy_arduino[0] > jongsu_x:
            crazy_arduino[0] -= 1
        elif crazy_arduino[0] < jongsu_x:
            crazy_arduino[0] += 1
        if crazy_arduino[1] > jongsu_y:
            crazy_arduino[1] -= 1
        elif crazy_arduino[1] < jongsu_y:
            crazy_arduino[1] += 1
        if board[crazy_arduino[0]][crazy_arduino[1]] == 'I':
            return True
        elif board[crazy_arduino[0]][crazy_arduino[1]] == 'R':
            remove_arduino_position[crazy_arduino[0]][crazy_arduino[1]] = True
            exist_romove_arduino = True
            crazy_arduino[0] = -1
        else:
            board[crazy_arduino[0]][crazy_arduino[1]] = 'R'
    if exist_romove_arduino == True:
        for crazy_arduino in crazy_arduino_list:
            x,y = crazy_arduino
            if x <= -1:
                continue
            if remove_arduino_position[x][y] == True:
                board[x][y] = '.'
                crazy_arduino[0] = -1

    return False

def game(board,jongsu,crazy_arduino_list,command):
    l = len(command)
    for i in range(l):
        move_jongsu(board,jongsu,command[i])
        game_over = check_game_over(board,crazy_arduino_list,jongsu)
        if game_over == True:
            return i + 1
    return INF
               
            
move_cnt = game(board,jongsu,crazy_arduino_list,command)

if move_cnt == INF:
    for i in range(r):
        for j in range(c):
            print(board[i][j],end="")
        print()
else:
    print("kraj " + str(move_cnt))

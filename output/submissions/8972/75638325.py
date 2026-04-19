board = []

r,c = map(int,input().split())

for _ in range(r):
    board.append(list(input()))

jongsu = [-1,-1]
crazy_robot = []

for i in range(r):
    for j in range(c):
        if board[i][j] == 'I':
            jongsu = [i,j]
            board[i][j] = '.'
        elif board[i][j] == 'R':
            crazy_robot.append([i,j])
            board[i][j] = '.'

command_list = list(input())

kraj = False
answer = 0

dx = [0,1,1,1,0,0,0,-1,-1,-1]
dy = [0,-1,0,1,-1,0,1,-1,0,1]

for command in command_list:
    answer += 1
    crazy_robot_cnt = [[0]*c for _ in range(r)]
    k = int(command)
    jongsu[0] += dx[k]
    jongsu[1] += dy[k]
    for crazy_robot_x, crazy_robot_y in crazy_robot:
        if jongsu[0] > crazy_robot_x:
            crazy_robot_x += 1
        elif jongsu[0] < crazy_robot_x:
            crazy_robot_x -= 1
        if jongsu[1] > crazy_robot_y:
            crazy_robot_y += 1
        elif jongsu[1] < crazy_robot_y:
            crazy_robot_y -= 1
        if jongsu[0] == crazy_robot_x and jongsu[1] == crazy_robot_y:
            kraj = True
        else:
            crazy_robot_cnt[crazy_robot_x][crazy_robot_y] += 1
    if kraj == True:
        break
    else:
        crazy_robot = []
        for i in range(r):
            for j in range(c):
                if crazy_robot_cnt[i][j] == 1:
                    crazy_robot.append([i,j])
if kraj == True:
    print("kraj " + str(answer))
else:
    board[jongsu[0]][jongsu[1]] = 'I'
    for x,y in crazy_robot:
        board[x][y] = 'R'
    for i in range(r):
        for j in range(c):
            print(board[i][j],end="")
        print()
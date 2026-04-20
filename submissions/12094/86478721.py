def main():
    global n
    n = int(input())
    init_board = get_init_board()
    answer = dfs(init_board,0)
    print(answer)

def get_init_board():
    init_board = []
    for _ in range(n):
        init_board.append(list(map(int,input().split())))
    return init_board

def dfs(board,move_cnt):
    ret_value = 0
    if move_cnt == 5:
        return get_max_value(board)
    for command in range(4):
        new_board = get_new_board(board)
        play_game(new_board,command)
        ret_value = max(ret_value,dfs(new_board,move_cnt+1))
    return ret_value

def get_max_value(board):
    ret_value = 0
    for i in range(n):
        for j in range(n):
            ret_value = max(ret_value,board[i][j])
    return ret_value

def get_new_board(board):
    new_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[i][j]
    return new_board

def play_game(board,command):
    if command == 0:
        move_left(board)
    elif command == 1:
        move_right(board)
    elif command == 2:
        move_up(board)
    else:
        move_down(board)

def move_left(board):
    merge = [[False]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if board[x][y] == 0:
                continue
            move_block(board,merge,(x,y),0)

def move_right(board):
    merge = [[False]*n for _ in range(n)]
    for y in range(n-1,-1,-1):
        for x in range(n):
            if board[x][y] == 0:
                continue
            move_block(board,merge,(x,y),1)

def move_up(board):
    merge = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                continue
            move_block(board,merge,(x,y),2)

def move_down(board):
    merge = [[False]*n for _ in range(n)]
    for x in range(n-1,-1,-1):
        for y in range(n):
            if board[x][y] == 0:
                continue
            move_block(board,merge,(x,y),3)

def move_block(board,merge,start,direction):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    vx, vy = start
    nx, ny = start
    block_value = board[vx][vy]
    board[vx][vy] = 0
    while True:
        nx += dx[direction]
        ny += dy[direction]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or merge[nx][ny] == True:
            board[vx][vy] = block_value
            return
        elif board[nx][ny] != 0:
            if board[nx][ny] == block_value:
                merge[nx][ny] = True
                board[nx][ny] += block_value
            else:
                board[vx][vy] = block_value
            return
        else:
            vx = nx; vy = ny

if __name__ == "__main__":
    main()
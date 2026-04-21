def main():
    board = get_board(n)
    red = get_point(board,'R')
    blue = get_point(board,'B')
    answer = solution(board,red,blue,0)
    print(answer)

def get_board(n):
    board = []
    for _ in range(n): board.append(list(input()))
    return board

def get_point(board,c):
    for i in range(n):
        for j in range(m):
            if board[i][j] == c:return(i,j)

def solution(board,red,blue,cnt):
    if cnt == 10: return 0
    ret_value = 0
    red_x, red_y = red
    blue_x, blue_y = blue
    for move_type in range(4):
        new_red, new_blue = select_move_direction(board,red,blue,move_type)
        if new_red == red and new_blue == blue: continue
        new_red_x, new_red_y = new_red; new_blue_x, new_blue_y = new_blue
        if board[new_red_x][new_red_y] != 'R':
            if board[new_blue_x][new_blue_y] == 'B': return 1
        elif board[new_blue_x][new_blue_y] == 'O':
            board[new_red_x][new_red_y] = '.'
        else:
            ret_value = max(ret_value,solution(board,new_red,new_blue,cnt+1))
            board[new_blue_x][new_blue_y], board[new_red_x][new_red_y] = '.','.'
        board[red_x][red_y], board[blue_x][blue_y] = 'R','B'
    board[red_x][red_y], board[blue_x][blue_y] = 'R','B'
    return ret_value

def select_move_direction(board,red,blue,move_type):
    if move_type == 0: n_r, n_b = move_left(board,red,blue)
    elif move_type == 1: n_r, n_b = move_right(board,red,blue)
    elif move_type == 2: n_r, n_b = move_up(board,red,blue)
    else: n_r, n_b = move_down(board,red,blue)
    return n_r, n_b

def move_left(board,red,blue):
    red_x, red_y = red
    blue_x, blue_y = blue
    if blue_y < red_y:
        n_b = move_ball(board,blue,0)
        n_r = move_ball(board,red,0)
    else:
        n_r = move_ball(board,red,0)
        n_b = move_ball(board,blue,0)
    return n_r, n_b

def move_right(board,red,blue):
    red_x, red_y = red
    blue_x, blue_y = blue
    if blue_y > red_y:
        n_b = move_ball(board,blue,1)
        n_r = move_ball(board,red,1)
    else:
        n_r = move_ball(board,red,1)
        n_b = move_ball(board,blue,1)
    return n_r, n_b

def move_up(board,red,blue):
    red_x, red_y = red
    blue_x, blue_y = blue
    if blue_x < red_x:
        n_b = move_ball(board,blue,2)
        n_r = move_ball(board,red,2)
    else:
        n_r = move_ball(board,red,2)
        n_b = move_ball(board,blue,2)
    return n_r, n_b

def move_down(board,red,blue):
    red_x, red_y = red
    blue_x, blue_y = blue
    if blue_x > red_x:
        n_b = move_ball(board,blue,3)
        n_r = move_ball(board,red,3)
    else:
        n_r = move_ball(board,red,3)
        n_b = move_ball(board,blue,3)
    return n_r, n_b

def move_ball(board,ball,direction):
    x,y = ball
    ball_type = board[x][y]
    board[x][y] = '.'
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if board[nx][ny] == 'O': return (nx,ny)
        if board[nx][ny] != '.': board[x][y] = ball_type; break
        x,y = nx, ny
    return (x,y)

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
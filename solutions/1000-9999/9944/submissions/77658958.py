INF = int(1e9)

def main():
    case_idx = 0
    while True:
        try:
            case_idx += 1
            global n,m
            n,m = map(int,input().split())
            board = get_board()
            answer = INF
            for i in range(n):
                for j in range(m):
                    if board[i][j] == '*':
                        continue
                    board[i][j] = '#'
                    answer = min(answer,solution(board,(i,j),1))
                    board[i][j] = '.'
            if answer >= INF:
                answer = -1
            print("Case " + str(case_idx) + ": " + str(answer))
        except EOFError:
            break

def get_board():
    board = []
    for _ in range(n):
        board.append(list(input()))
    return board

def solution(board,start,move_cnt):
    ret_value = INF
    ret_value_zero = True
    x,y = start
    if x > 0 and board[x-1][y] == '.':
        ret_value_zero = False
        new_start = move_ball(board,start,(-1,0))
        if game_over(board) == True: 
            cancel_move(board,start,new_start,(-1,0))
            return move_cnt
        ret_value = min(ret_value,solution(board,new_start,move_cnt+1))
        cancel_move(board,start,new_start,(-1,0))

    if y > 0 and board[x][y-1] == '.':
        ret_value_zero = False
        new_start = move_ball(board,start,(0,-1))
        if game_over(board) == True:
            cancel_move(board,start,new_start,(0,-1))
            return move_cnt
        ret_value = min(ret_value,solution(board,new_start,move_cnt+1))
        cancel_move(board,start,new_start,(0,-1))

    if x < n-1 and board[x+1][y] == '.':
        ret_value_zero = False
        new_start = move_ball(board,start,(1,0))
        if game_over(board) == True:
            cancel_move(board,start,new_start,(1,0))
            return move_cnt
        ret_value = min(ret_value,solution(board,new_start,move_cnt+1))
        cancel_move(board,start,new_start,(1,0))

    if y < m-1 and board[x][y+1] == '.':
        ret_value_zero = False
        new_start = move_ball(board,start,(0,1))
        if game_over(board) == True:
            cancel_move(board,start,new_start,(0,1))
            return move_cnt
        ret_value = min(ret_value,solution(board,new_start,move_cnt+1))
        cancel_move(board,start,new_start,(0,1))
    if move_cnt == 1 and ret_value_zero == True:
        ret_value = 0
    return ret_value

def move_ball(board,start,direction):
    dx,dy = direction
    x,y = start
    while True:
        board[x][y] = '#'
        nx = x + dx; ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] != '.':
            return x,y
        x = nx; y = ny

def game_over(board):
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                return False
    return True

def cancel_move(board,start,end,direction):
    x,y = start
    dx, dy = direction
    while True:
        x += dx
        y += dy
        board[x][y] = '.'
        if x == end[0] and y == end[1]:
            return

if __name__ == "__main__":
    main()
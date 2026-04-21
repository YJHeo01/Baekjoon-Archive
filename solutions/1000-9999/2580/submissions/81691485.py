def main():
    board = get_board()
    row_state, column_state, box_state = init_state(board)
    solution(board,row_state,column_state,box_state,(0,0))

def get_board():
    board = []
    for _ in range(9):
        board.append(list(map(int,input().split())))
    return board

def init_state(board):
    row_state = [[False]*10 for _ in range(9)]
    column_state = [[False]*10 for _ in range(9)]
    box_state = [[False]*10 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            row_state[i][board[i][j]] = True
            column_state[j][board[i][j]] = True
            box_state[get_box_idx((i,j))][board[i][j]] = True
    return row_state, column_state, box_state

def get_box_idx(point):
    x,y = point
    return (x // 3) * 3 + y // 3

def solution(board,row_state,column_state,box_state,point):
    x,y = point
    if x == 9:
        print_board(board)
        exit(0)
    nx,ny = get_next_point(x,y)
    if board[x][y] == 0:
        box_idx = get_box_idx((x,y))
        for i in range(1,10):
            if row_state[x][i] or column_state[y][i] or box_state[box_idx][i]: continue
            row_state[x][i], column_state[y][i], box_state[box_idx][i] = True,True,True
            board[x][y] = i
            solution(board,row_state,column_state,box_state,(nx,ny))
            board[x][y] = 0
            row_state[x][i], column_state[y][i], box_state[box_idx][i] = False,False,False
    else:
        solution(board,row_state,column_state,box_state,(nx,ny))
        
    
def get_next_point(x,y):
    y += 1
    if y == 9:
        return (x+1,0)
    return x,y

def print_board(board):
    for tmp in board:
        print(*tmp)

if __name__ == "__main__":
    main()
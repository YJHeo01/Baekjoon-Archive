def block_type_cnt(board):
    O_cnt = 0; X_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O_cnt += 1
            elif board[i][j] == 'X':
                X_cnt += 1
            else:
                continue
    return O_cnt, X_cnt

def check_three_combo(board,block_type):
    for i in range(3):
        if board[i][0] == block_type and board[i][1] == block_type and board[i][2] == block_type:
            return True
        if board[0][i] == block_type and board[1][i] == block_type and block_type == board[2][i]:
            return True
    if board[0][0] == block_type and board[1][1] == block_type and block_type == board[2][2]:
        return True
    if board[2][0] == block_type and board[1][1] == block_type and block_type == board[0][2]:
        return True
    return False

def check_full_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                return False
    return True

def check_vaild(board):
    O_cnt, X_cnt = block_type_cnt(board)
    if O_cnt == X_cnt:
        if check_three_combo(board,'O') == True and check_three_combo(board,'X') == False:
            return True
        return False
    elif O_cnt + 1 == X_cnt:
        if check_three_combo(board,'O') == True:
            return False
        if check_three_combo(board,'X') == True or check_full_board(board) == True:
            return True
        return False
    else:
        return False
    
while True:
    test_case = list(input())
    if test_case[0] == 'e':
        break
    board = []
    for i in range(3):
        board.append(test_case[i*3:(i+1)*3])
    valid = check_vaild(board)
    if valid == True:
        print("valid")
    else:
        print("invalid")
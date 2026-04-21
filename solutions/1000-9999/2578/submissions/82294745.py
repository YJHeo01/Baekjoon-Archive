def main():
    board = [list(map(int,input().split())) for _ in range(5)]
    line_up = [list(map(int,input().split())) for _ in range(5)]
    position = get_position(board)
    print(solution(board,position,line_up))
    

def get_position(board):
    position = [[0,0] for _ in range(26)]    
    for i in range(5):
        for j in range(5):
            position[board[i][j]] = [i,j]
    return position

def solution(board,position,line_up):
    bingo_cnt = 0
    row_bingo = [False] * 5
    column_bingo = [False] * 5
    leftHighToRightLow_bingo = False
    rightHighToLeftLow_bingo = False
    answer = 1
    for i in range(5):
        for j in range(5):
            x,y = position[line_up[i][j]]
            board[x][y] = 0
            if row_bingo[x] == False and check_row_bingo(board,x):
                bingo_cnt += 1
                row_bingo[x] = True
            if column_bingo[y] == False and check_column_bingo(board,y):
                bingo_cnt += 1
                column_bingo[y] = True
            if x == y and leftHighToRightLow_bingo == False and leftHighToRightLow(board):
                bingo_cnt += 1
                leftHighToRightLow_bingo = True
            if x + y == 4 and rightHighToLeftLow_bingo == False and rightHighToLeftLow(board):
                bingo_cnt += 1
                rightHighToLeftLow_bingo = True
            if bingo_cnt >= 3:
                return answer
            answer += 1
    return answer

def check_row_bingo(board,row):
    for column in range(5):
        if board[row][column] != 0:
            return False
    return True

def check_column_bingo(board,column):
    for row in range(5):
        if board[row][column] != 0:
            return False
    return True

def leftHighToRightLow(board):
    for i in range(5):
        if board[i][i] != 0:
            return False
    return True

def rightHighToLeftLow(board):
    for i in range(5):
        if board[i][4-i] != 0:
            return False
    return True

if __name__ == "__main__":
    main()
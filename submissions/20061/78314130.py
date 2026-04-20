import sys

input = sys.stdin.readline

def main():
    green = [[False]*4 for _ in range(6)]
    blue = [[False]*6 for _ in range(4)]
    solution(green,blue)

def solution(green,blue):
    n = int(input())
    score = 0
    for _ in range(n):
        t,x,y = map(int,input().split())
        if t == 1:
            get_new_blue_block(blue,x,x)
            get_new_green_block(green,y,y)
        elif t == 2:
            get_new_green_block(green,y,y+1)
            y = get_new_blue_block(blue,x,x)
            blue[x][y-1] = True
        else:
            get_new_blue_block(blue,x,x+1)
            x = get_new_green_block(green,y,y)
            green[x-1][y] = True
        score += get_blue_board_score(blue)
        score += get_green_board_score(green)
        special_row(green); special_column(blue)
    cnt = get_cnt(green) + get_cnt(blue)
    print(score)
    print(cnt)

def get_new_blue_block(blue,x1,x2):
    y = 2
    while True:
        if y > 5 or blue[x1][y] == True or blue[x2][y] == True: break
        y += 1
    y -= 1
    blue[x1][y] = True; blue[x2][y] = True
    return y

def get_new_green_block(green,y1,y2):
    x = 2
    while True:
        if x > 5 or green[x][y1] == True or green[x][y2] == True: break
        x += 1
    x -= 1
    green[x][y1] = True; green[x][y2] = True
    return x

def get_blue_board_score(blue):
    start = 5; end = -1; ret_value = 0
    for column in range(start,end,-1):
        while True:
            if check_full_column(blue,column) == False: break
            ret_value += 1; end += 1
            erase_column(blue,column)
            move_blue_block(blue,column)
    return ret_value

def check_full_column(board,column):
    for row in range(4):
        if board[row][column] == False: return False
    return True

def erase_column(blue,column):
    for row in range(4): blue[row][column] = False
    return blue

def move_blue_block(blue,start_column):
    for column in range(start_column,0,-1):
        for row in range(4):
            if blue[row][column-1] == True:
                blue[row][column] = True
                blue[row][column-1] = False
    return blue 

def get_green_board_score(green):
    start = 5; end = -1; ret_value = 0
    for row in range(start,end,-1):
        while True:
            if check_full_row(green,row) == False: break
            ret_value += 1; end += 1
            erase_row(green,row)
            move_green_block(green,row)
    return ret_value

def erase_row(green,row):
    for column in range(4): green[row][column] = False
    return green

def move_green_block(green,start_row):
    for row in range(start_row,0,-1):
        for column in range(4):
            if green[row-1][column] == True:
                green[row][column] = True
                green[row-1][column] = False
    return green

def check_full_row(green,row):
    for column in range(4):
        if green[row][column] == False: return False
    return True

def special_row(green):
    for row in range(2):
        if empty_row(green,row) == False:
            erase_row(green,5)
            move_green_block(green,5)

def empty_row(green,row):
    for column in range(4):
        if green[row][column] == True: return False
    return True

def special_column(blue):
    for column in range(2):
        if empty_column(blue,column) == False:
            erase_column(blue,5)
            move_blue_block(blue,5)

def empty_column(blue,column):
    for row in range(4):
        if blue[row][column] == True: return False
    return True

def get_cnt(board):
    ret_value = 0
    for row in board:
        for column in row:
            if column == True: ret_value += 1
    return ret_value

if __name__ == "__main__":
    main()
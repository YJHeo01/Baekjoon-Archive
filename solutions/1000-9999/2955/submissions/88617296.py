def main():
    box_pos = set_box_pos()
    row = [[False]*10 for _ in range(9)]
    column = [[False]*10 for _ in range(9)]
    box = [[False]*10 for _ in range(9)]
    sudoku = [list(input()) for _ in range(9)]
    finish = [[False]*9 for _ in range(9)]
    
    while True:
        state = min(cross(sudoku,row,column,box,finish),hatching(sudoku,box_pos,box,row,column))
        if state <= 0: break
    
    if state < 0:
        print("ERROR")
    else:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j],end="")
            print()

def set_box_pos():
    box_pos = []
    for i in range(3):
        for j in range(3):
            box_pos.append((i*3,j*3,i*3+3,j*3+3))
    return box_pos

def get_box_idx(x,y):
    return x // 3 * 3 + y // 3

def cross(sudoku,row,column,box,finish):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == '.' or finish[x][y]: continue
            finish[x][y] = True
            value = int(sudoku[x][y])
            box_idx = get_box_idx(x,y)
            #if row[x][value] or column[y][value] or box[box_idx][value]: return -1
            row[x][value], column[y][value], box[box_idx][value] = True, True, True
    return 1

def hatching(sudoku,box_pos,box,row,column):
    ret_value = 0
    for box_idx in range(9):
        start_x,start_y,end_x,end_y = box_pos[box_idx]
        for value in range(1,10):
            if box[box_idx][value]: continue
            target_x, target_y = -1,-1
            for x in range(start_x,end_x):
                for y in range(start_y,end_y):
                    if sudoku[x][y] != '.' or row[x][value] or column[y][value]: continue
                    if target_x == -1:
                        target_x, target_y = x,y
                    else:
                        target_x, target_y = -2,-2
            if target_x == -1: return -1
            if target_x < 0: continue
            ret_value = 1
            sudoku[target_x][target_y] = str(value)
            box[box_idx][value], row[target_x][value], column[target_y][value] = True, True, True
    return ret_value
                
if __name__ == "__main__":
    main()
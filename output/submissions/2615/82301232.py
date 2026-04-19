def main():
    board = [list(map(int,input().split())) for _ in range(19)]
    x,y = solution(board)
    if x == -1 and y == -1:
        print(0)
        exit(0)
    print(board[x][y])
    print(x+1,y+1)

def solution(board):
    row_visited = [[0]* 19 for _ in range(19)]
    column_visited = [[0]*19 for _ in range(19)]
    leftToRight_visited = [[0]*19 for _ in range(19)]
    rightToLeft_visited = [[0]*19 for _ in range(19)]
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            if row_visited[i][j] == 0 and check_row_bingo(board,row_visited,(i,j)) == 5:
                return (i,j)
            if column_visited[i][j] == 0 and check_column_bingo(board,column_visited,(i,j)) == 5:
                return (i,j)
            if leftToRight_visited[i][j] == 0 and check_leftToRight_bingo(board,leftToRight_visited,(i,j)) == 5:
                return (i,j)
            if rightToLeft_visited[i][j] == 0 and check_rightToLeft_bingo(board,rightToLeft_visited,(i,j)) == 5:
                return (i+4,j-4)
    return (-1,-1)

def check_row_bingo(board,visited,start):
    x,y = start
    if y == 18 or board[x][y+1] != board[x][y]:
        return visited[x][y] + 1
    visited[x][y+1] = visited[x][y] + 1
    return check_row_bingo(board,visited,(x,y+1))

def check_column_bingo(board,visited,start):
    x,y = start
    if x == 18 or board[x+1][y] != board[x][y]:
        return visited[x][y] + 1
    visited[x+1][y] = visited[x][y] + 1
    return check_column_bingo(board,visited,(x+1,y))

def check_leftToRight_bingo(board,visited,start):
    x,y = start
    if x == 18 or y == 18 or board[x+1][y+1] != board[x][y]:
        return visited[x][y] + 1
    visited[x+1][y+1] = visited[x][y] + 1
    return check_leftToRight_bingo(board,visited,(x+1,y+1))

def check_rightToLeft_bingo(board,visited,start):
    x,y = start
    if x == 18 or y == 0 or board[x+1][y-1] != board[x][y]:
        return visited[x][y] + 1
    visited[x+1][y-1] = visited[x][y] + 1
    return check_rightToLeft_bingo(board,visited,(x+1,y-1))

if __name__ == "__main__":
    main()
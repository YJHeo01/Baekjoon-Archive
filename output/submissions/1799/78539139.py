def main():
    board = get_board()
    impossible_new_bishop = [[0]*n for _ in range(n)]
    answer = solution(board,impossible_new_bishop,(0,0),0)
    print(answer)

def get_board():
    board = []
    for _ in range(n): board.append(list(map(int,input().split())))
    return board

def solution(board,impossible_new_bishop,point,bishop_cnt):
    x,y = point
    if x == n: return bishop_cnt
    nx,ny = get_next_point(x,y)
    ret_value = bishop_cnt
    if board[x][y] == 1 and impossible_new_bishop[x][y] == 0:
        make_new_bishop(impossible_new_bishop,point)
        ret_value = max(ret_value,solution(board,impossible_new_bishop,(nx,ny),bishop_cnt+1))
        remove_bishop(impossible_new_bishop,point)
    ret_value = max(ret_value,solution(board,impossible_new_bishop,(nx,ny),bishop_cnt))
    return ret_value

def get_next_point(x,y):
    if y == n-1: return (x+1,0)
    else: return (x,y+1)

def make_new_bishop(impossible_new_bishop,point):
    x,y = point
    dx = 1
    dy_list = [-1,1]
    for i in range(2):
        nx, ny = x,y
        dy = dy_list[i]
        while True:
            nx += dx; ny += dy
            if ny < 0 or nx >= n or ny >= n: break
            impossible_new_bishop[nx][ny] += 1

def remove_bishop(impossible_new_bishop,point):
    x,y = point
    dx = 1
    dy_list = [-1,1]
    for i in range(2):
        nx, ny = x,y
        dy = dy_list[i]
        while True:
            nx += dx; ny += dy
            if ny < 0 or nx >= n or ny >= n: break
            impossible_new_bishop[nx][ny] -= 1

if __name__ == "__main__":
    n = int(input())
    main()
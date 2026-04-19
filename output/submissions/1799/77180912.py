n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

bishop = [[False]*n for _ in range(n)]

def check_make_new_bissop(bisshop,point):
    x,y = point
    dx = [-1,-1]
    dy = [-1,1]
    ret_value = True
    for i in range(2):
        nx, ny = x,y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break
            if bisshop[nx][ny] == True:
                return False
    return ret_value


def get_next_point(x,y):
    if y == n-1:
        return (x+1,0)
    else:
        return (x,y+1)

def solution(board,bishop,point,bishop_cnt):
    x,y = point
    if x == n:
        return bishop_cnt
    nx,ny = get_next_point(x,y)
    ret_value = solution(board,bishop,(nx,ny),bishop_cnt)
    if board[x][y] == 1 and check_make_new_bissop(bishop,(x,y)) == True:
        bishop[x][y] = True
        ret_value = max(ret_value,solution(board,bishop,(nx,ny),bishop_cnt+1))
        bishop[x][y] = False
    return ret_value
    
answer = solution(board,bishop,(0,0),0)

print(answer)
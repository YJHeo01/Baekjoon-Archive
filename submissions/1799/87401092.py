import sys

input = sys.stdin.readline

def main():
    down_right_dia = [[False]*n for _ in range(n)] #좌측 상단에서 우측 하단으로 내려가는 대각선에 중복된 비숍 유무 체크
    up_left_dia = [False]*(2*n) #우측 상단에서 좌측 하단으로 내려가는 대각선에 중복된 비숍 유무 체크
    board = [list(map(int,input().split())) for _ in range(n)]
    answer = backtracking(board,down_right_dia,up_left_dia,(0,0))
    print(answer)

def backtracking(board,down_right_dia,up_left_dia,point):
    x,y = point
    if x == n: return 0
    ret_value = backtracking(board,down_right_dia,up_left_dia,get_nx_ny(x,y))
    
    d_i,d_j = x-y,0
    if d_i < 0: #좌-상 -> 우-하 대각선의 비숍들은 x,y의 차가 같다.
        d_j = -d_i
        d_i = 0

    u_i = x + y #우-상 -> 좌-하 대각선의 비숍들은 x + y값이 같다

    if board[x][y] == 1 and down_right_dia[d_i][d_j] == False and up_left_dia[u_i] == False:
        down_right_dia[d_i][d_j] = True
        up_left_dia[u_i] = True
        ret_value = max(ret_value,1+backtracking(board,down_right_dia,up_left_dia,get_nx_ny(x,y)))
        up_left_dia[u_i] = False
        down_right_dia[d_i][d_j] = False
    
    return ret_value
    

def get_nx_ny(x,y):
    if y + 1 == n:
        return (x+1,0)
    else:
        return (x,y+1)

if __name__ == "__main__":
    n = int(input())
    main()
n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j].isdigit() == True:
            board[i][j] = int(board[i][j])
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

INF = int(1e9)

def solution(board,dp,start):
    x,y = start
    dx = [0,board[x][y],0,-board[x][y]]
    dy = [board[x][y],0,-board[x][y],0]
    ret_value = dp[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or type(board[nx][ny]) == str:
            continue
        if dp[nx][ny] == 0:
            dp[nx][ny] = dp[x][y] + 1
            ret_value = max(solution(board,dp,(nx,ny)),ret_value)
            if ret_value < INF:
                dp[nx][ny] = 0
            else:
                return ret_value
        elif dp[nx][ny] < dp[x][y]:
            return INF
        else:
            continue
    return ret_value

answer = solution(board,dp,(0,0))

if answer >= INF:
    answer = -1

print(answer)
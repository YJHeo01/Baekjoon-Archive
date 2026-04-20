#https://github.com/YJHeo01
#https://www.acmicpc.net/problem/1890

n = int(input())

game_board = []

for _ in range(n):
    game_board.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]

dp[0][0] = 1
dx = [0,1]
dy = [1,0]

for y in range(n):
    for x in range(n):
        if dp[y][x] == 0 or game_board[y][x] == 0:
            continue
        for k in range(2):
            nx = x + game_board[y][x] * dx[k]
            ny = y + game_board[y][x] * dy[k]
            if nx >= n or ny >= n:                
                continue
            dp[ny][nx] += dp[y][x]

print("cut")

for i in range(n):
    for j in range(n):
        print(dp[i][j],end=" ")
    print()
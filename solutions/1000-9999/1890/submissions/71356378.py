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
        if dp[y][x] == 0: #점프를 해도 방문할 경우가 없음
            continue
        for k in range(2):
            nx = x + game_board[y][x] * dx[k]
            ny = y + game_board[y][x] * dy[k]
            if nx >= n or ny >= n:
                continue
            dp[ny][nx] += 1

answer = dp[n-1][n-1] - 2 #칸에 적힌 수가 0이고, k를 이용한 for문으로 인해 실제 경로의 개수보다 2 높게 나옴
print(answer)
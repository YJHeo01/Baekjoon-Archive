n,m,t = map(int,input().split())

board = [[0]]

for _ in range(n):
    board.append(list(map(int,input().split())))

move_factor = [0] * (n+1)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(t):
    x,d,k = map(int,input().split())
    for i in range(x,n+1,x):
        if d == 0:
            move_factor[i] -= k
        else:
            move_factor[i] += k
    adj_number = [[False]*m for _ in range(n+1)]
    no_remove = True
    for vx in range(1,n+1):
        for i in range(m):
            if board[vx][i] == 0:
                continue
            if board[vx][i] == board[vx][i-1]:
                adj_number[vx][i] = True
                adj_number[vx][i-1] = True
                no_remove = False
    for vx in range(1,n):
        nx = vx + 1
        for i in range(m):
            vy = (i + move_factor[vx]) % m
            if board[vx][vy] == 0:
                continue
            ny = (i + move_factor[nx]) % m
            if board[vx][vy] == board[nx][ny]:
                adj_number[vx][vy] = True
                adj_number[nx][ny] = True
                no_remove = False
    if no_remove == False:
        for i in range(1,n+1):
            for j in range(m):
                if adj_number[i][j] == True:
                    board[i][j] = 0
    else:
        sum_value = 0
        value_cnt = 0
        for i in range(1,n+1):
            for j in range(m):
                if board[i][j] >= 1:
                    sum_value += board[i][j]
                    value_cnt += 1
        if value_cnt == 0:
            break
        avg_value = sum_value / value_cnt
        for i in range(1,n+1):
            for j in range(m):
                if board[i][j] <= 0:
                    continue
                if board[i][j] > avg_value:
                    board[i][j] -= 1
                elif board[i][j] < avg_value:
                    board[i][j] += 1

answer = 0

for i in range(1,n+1):
    for j in range(m):
        if board[i][j] != 0:
            answer += board[i][j]

print(answer)
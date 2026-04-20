n,m = map(int,input().split())
board = []
for i in range(n):
    tmp = list(input())
    board.append(tmp)
cnt = 2501
for i in range(n-7):
    for j in range(m-7):
        tmp = 0
        for k in range(8):
            for p in range(8):
                if (i+k + j+p) % 2 == 0:
                    if board[i+k][j+p] == 'W':
                        tmp += 1
                else:
                    if board[i+k][j+p] == 'B':
                        tmp += 1
        tmp = min(tmp,64-tmp)
        cnt = min(cnt,tmp)

print(cnt)
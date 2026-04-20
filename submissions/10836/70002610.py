import sys

input = sys.stdin.readline

m,n = map(int,input().split())
    
board = [[1] * m for _ in range(m)]

while n:
    dx = [[0]*m for _ in range(m)]
    num_list = list(map(int,input().split()))
    idx = 0
    for i in range(3):
        for j in range(num_list[i]):
            if idx < m:
                dx[m-1-idx][0] = i
            else:
                dx[0][idx-m+1] = i
            idx += 1
    for i in range(1,m):
        for j in range(1,m):
            dx[i][j] = max(dx[i-1][j-1],dx[i-1][j],dx[i][j-1])
            board[i][j] += dx[i][j]
    for i in range(m):
        board[0][i] += dx[0][i]
    
    for i in range(1,m):
        board[i][0] += dx[i][0]
    n-=1

for i in range(m):
    for j in range(m):
        print(board[i][j],end=" ")
    print()
        
import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

n,m = m,n

maze = [list(input()) for _ in range(n)]

dp_A = [[0]*m for _ in range(n)]
dp_B = [[0]*m for _ in range(n)]

dp_A[0][0] = 1
dp_B[n-1][m-1] = 1

INF = int(1e9) + 7

for i in range(n):
    for j in range(m):
        if maze[i][j] == '1': continue
        if i != 0: dp_A[i][j] += dp_A[i-1][j]
        if j != 0: dp_A[i][j] += dp_A[i][j-1]
        dp_A[i][j] %= INF

for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if maze[i][j] == '1': continue
        if i != n-1: dp_B[i][j] += dp_B[i+1][j]
        if j != m-1: dp_B[i][j] += dp_B[i][j+1]
        dp_B[i][j] %= INF

answer = dp_A[n-1][m-1]


for _ in range(k):
    y1,x1,y2,x2 = map(int,input().split())
    if not ((y1 == y2 and x1 + 1 == x2) or (x1 == x2 and y1 + 1 == y2)): answer += dp_A[x1][y1] * dp_B[x2][y2]
    if not ((y1 == y2 and x2 + 1 == x1) or (x1 == x2 and y2 + 1 == y1)): answer += dp_B[x1][y1] * dp_A[x2][y2]
    answer %= INF
    
print(answer)
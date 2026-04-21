INF = int(1e9)

n,m = map(int,input().split())

moon = []
for _ in range(n):
    moon.append(list(map(int,input().split())))

idx = 0

dp_L = [[INF]*m for _ in range(n+1)]
dp_C = [[INF]*m for _ in range(n+1)]
dp_R = [[INF]*m for _ in range(n+1)]

for i in range(m):
    dp_L[0][i] = 0
    dp_C[0][i] = 0
    dp_R[0][i] = 0


for i in range(n):
    for j in range(m):
        if j != m-1:
            dp_L[i+1][j] = min(dp_C[i][j+1] + moon[i][j],dp_R[i][j+1] + moon[i][j])
        if j != 0 and j != m-1:
            dp_C[i+1][j] = min(dp_L[i][j] + moon[i][j],dp_R[i][j] + moon[i][j])
        elif j == 0:
            dp_C[i+1][j] = dp_L[i][j] + moon[i][j]
        else:
            dp_C[i+1][j] = dp_R[i][j] + moon[i][j]
        if j != 0:
            dp_R[i+1][j] = min(dp_L[i][j-1] + moon[i][j],dp_C[i][j-1] + moon[i][j])

answer = INF

answer = min(dp_C[n]+dp_L[n]+dp_R[n])

print(answer)
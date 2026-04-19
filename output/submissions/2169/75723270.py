import sys

input = sys.stdin.readline

n,m = map(int,input().split())

planet = []

for _ in range(n):
    planet.append(list(map(int,input().split())))

dp_R_to_L = [[0]*m for _ in range(n)]
dp_L_to_R = [[0]*m for _ in range(n)]

dp_L_to_R[0][0] = planet[0][0]

for i in range(1,m):
    dp_L_to_R[0][i] = planet[0][i] + dp_L_to_R[0][i-1]

for i in range(1,n):
    dp_R_to_L[i][m-1] = max(dp_R_to_L[i-1][m-1],dp_L_to_R[i-1][m-1]) + planet[i][m-1]
    dp_L_to_R[i][0] = max(dp_L_to_R[i-1][0],dp_R_to_L[i-1][0]) + planet[i][0]
    for j in range(1,m):
        dp_L_to_R[i][j] = max(dp_L_to_R[i-1][j],dp_R_to_L[i-1][j],dp_L_to_R[i][j-1]) + planet[i][j]
    for j in range(m-2,-1,-1):
        dp_R_to_L[i][j] = max(dp_L_to_R[i-1][j],dp_R_to_L[i-1][j],dp_R_to_L[i][j+1]) + planet[i][j]
    

print(max(dp_L_to_R[n-1][m-1],dp_R_to_L[n-1][m-1]))
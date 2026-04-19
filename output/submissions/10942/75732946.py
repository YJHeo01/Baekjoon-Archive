import sys

input = sys.stdin.readline
n = int(input())

board = list(map(int,input().split()))


dp = [[False]*n for _ in range(n)]
for i in range(n):
    left, right = i,i
    while True:
        dp[left][right] = True
        left -= 1; right += 1
        if left < 0 or right >= n or board[left] != board[right]:
            break


for i in range(1,n):
    left, right = i-1, i
    while True:
        dp[left][right] = True
        left -= 1; right += 1
        if left < 0 or right >= n or board[left] != board[right]:
            break

m = int(input())

for _ in range(m):
    s,e = map(int,input().split())
    if dp[s-1][e-1] == True:
        print(1)
    else:
        print(0)
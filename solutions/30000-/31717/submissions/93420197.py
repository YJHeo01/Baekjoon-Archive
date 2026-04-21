import sys

input = sys.stdin.readline

m,k = map(int,input().split())

num_list = list(map(int,input().split()))

high = []
low = []

for _ in range(m):
    high.append(list(input().rstrip()))
    low.append(list(input().rstrip()))
    
tmp_high = []
tmp_low = []

for num in num_list:
    tmp_high += high[num-1]
    tmp_low += low[num-1]
    
track = [tmp_high,tmp_low]

length = len(tmp_high)

INF = int(1e9)

dp = [[INF]*length for _ in range(2)]

if track[0][0] != '#': dp[0][0] = 0

if track[1][0] != '#': dp[1][0] = 0

for i in range(1,length):
    if track[0][i-1] != '#' and track[1][i-1] != '#':
        dp[1][i-1] = min(dp[1][i-1],dp[0][i-1]+1)
        dp[0][i-1] = min(dp[1][i-1]+1,dp[0][i-1])
    if track[0][i] != '#':
        dp[0][i] = min(dp[0][i],dp[0][i-1]+1)
    if track[1][i] != '#':
        dp[1][i] = min(dp[1][i],dp[1][i-1]+1)

answer = min(dp[0][length-1],dp[1][length-1])

if answer >= INF:
    answer = -1

print(answer)
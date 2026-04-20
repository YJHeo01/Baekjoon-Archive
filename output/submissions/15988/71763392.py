import sys

input = sys.stdin.readline

t = int(input())

num_list = []

for _ in range(t):
    num_list.append(int(input()))
size = max(max(num_list)+1,4)
dp = [0] * size
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,size):
    dp[i] += (dp[i-1]+dp[i-2]+dp[i-3])
    dp[i] %= 1000000009

for i in num_list:
    print(dp[i])
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * n

num_list = list(map(int,input().split()))

for i in range(0,n):
    dp[i] = max(dp[i]+num_list[i],num_list[i])

print(max(dp))
import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    value_sum = 0
    coin_list = []
    for _ in range(n):
        value, cnt = map(int,input().split())
        value_sum += value * cnt
        coin_list.append([value,cnt])
    if value_sum % 2 == 1:
        print(0)
        continue
    target_value = value_sum // 2
    dp = [[0]*(target_value+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        value, cnt = coin_list[i-1]
        for j in range(target_value):
            if dp[i-1][j] == 1:
                dp[i][j] = 1
                for k in range(1,cnt+1):
                    if j + value * k > target_value:
                        break
                    dp[i][j+value*k] = 1
    print(dp[n][target_value])
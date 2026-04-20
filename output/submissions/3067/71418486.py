#https://github.com/YJHeo01

t = int(input())

for _ in range(t):
    answer = 0
    n = int(input())
    coin_list = list(map(int,input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    for coin in coin_list:
        for i in range(1,m+1):
            if dp[i-coin] != 0:
                dp[i] += dp[i-coin]
    print(dp[m])
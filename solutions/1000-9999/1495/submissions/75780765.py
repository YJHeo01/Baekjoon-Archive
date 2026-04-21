n,s,m = map(int,input().split())

_list = list(map(int,input().split()))
dp = [[False] * (m+1) for _ in range(n+1)]

dp[0][s] = True

for idx in range(n):
    for value in range(m+1):
        if dp[idx][value] == True:
            next_value_A = value + _list[idx]
            next_value_B = value - _list[idx]
            if next_value_A <= m:
                dp[idx+1][next_value_A] = True
            if next_value_B >= 0:
                dp[idx+1][next_value_B] = True

answer = -1

for i in range(m,-1,-1):
    if dp[n][i] == True:
        answer = i
        break

print(answer)
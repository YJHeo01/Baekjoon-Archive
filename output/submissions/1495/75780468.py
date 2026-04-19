n,s,m = map(int,input().split())

_list = list(map(int,input().split()))
dp = [-1] * (m+1)

dp[s] = 0

for idx in range(n):
    for value in range(m+1):
        if dp[value] == idx:
            next_value_A = value + _list[idx]
            next_value_B = value - _list[idx]
            if next_value_A <= m:
                dp[next_value_A] = idx + 1
            if next_value_B >= 0:
                dp[next_value_B] = idx + 1

answer = -1

for i in range(m,-1,-1):
    if dp[i] == n:
        answer = i
        break

print(answer)
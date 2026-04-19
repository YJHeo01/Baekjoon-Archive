INF = 4000000

plus_dp = [0] * (INF+1)
minus_dp = [0] * (INF+1)
plus_dp[0], minus_dp[0] = 1,1
max_plus, max_minus = 0,0

n,s = map(int,input().split())

array = list(map(int,input().split()))

zero_cnt = 0

for i in array:
    if i > 0:
        max_plus += i
        for j in range(max_plus,-1,-1):
            if plus_dp[j] <= 0: continue
            plus_dp[j+i] += plus_dp[j]
    elif i < 0:
        i *= -1
        max_minus += i
        for j in range(max_minus,-1,-1):
            if minus_dp[j] <= 0: continue
            minus_dp[j+i] += minus_dp[j]
    else:
        zero_cnt += 1

answer = 0

if s >= 0:
    for plus in range(s,max_plus+1):
        minus = plus - s
        if minus > max_minus: break
        answer += plus_dp[plus] * minus_dp[minus]
else:
    s *= -1
    for minus in range(s,max_minus+1):
        plus = minus - s
        if plus > max_plus: break
        answer += plus_dp[plus] * minus_dp[minus]

answer <<= zero_cnt
if s == 0: answer -= 1


print(answer)
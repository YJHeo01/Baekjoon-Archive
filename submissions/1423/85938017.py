n = int(input())
cnt = list(map(int,input().split()))
power = list(map(int,input().split()))
d = int(input())
sum_of_power = [0] * (d+1)
dp = [[0]*n for _ in range(d+1)]

for i in range(n):
    sum_of_power[0] += cnt[i] * power[i]
    dp[0][i] = cnt[i]

for day in range(1,d+1):
    for level in range(n):
        dp[day][level] = dp[day-1][level]
    sum_of_power[day] = sum_of_power[day-1]
    for level_up in range(n-1,0,-1):
        if level_up > day: continue
        last_day = day - level_up
        for next_level in range(level_up,n):
            cur_level = next_level - level_up
            if dp[last_day][cur_level] == 0: continue
            if sum_of_power[last_day] - power[cur_level] + power[next_level] >= sum_of_power[day]:
                sum_of_power[day] = sum_of_power[last_day] - power[cur_level] + power[next_level]
                for level in range(n):
                    dp[day][level] = dp[last_day][level]
                dp[day][cur_level] -= 1; dp[day][next_level] += 1

print(sum_of_power[d])
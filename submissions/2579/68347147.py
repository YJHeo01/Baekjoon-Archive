n = int(input())

dp = [0] * (n+1)

stair = [0]

for i in range(n):
    tmp = int(input())
    stair.append(tmp)
for i in range(1,n+1):
    if i == 1:
        dp[1] = stair[1]
    elif i == 2: dp[2] = stair[1] + stair[2]
    elif i == 3: dp[3] = max(stair[2]+stair[3],stair[1]+stair[3])
    elif i == 4:dp[4] = max(stair[4]+dp[2],stair[4]+stair[3]+dp[1])
    else :
        for i in range(5,n+1):
            dp[i] = stair[i]
            dp[i] += max(stair[i-1]+dp[i-3],stair[i-2]+stair[i-3]+dp[i-5],stair[i-2]+dp[i-4])

print(dp[n])
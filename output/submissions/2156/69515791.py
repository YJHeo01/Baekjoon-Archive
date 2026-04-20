n = int(input())

num_list = []
dp = [0] * (n+3)
for i in range(n):
    tmp = int(input())
    num_list.append(tmp)
    dp[i] = tmp

num_list = num_list + [0,0]

for i in range(n):
    dp[i] += max(dp[i-3]+num_list[i-1],dp[i-2])


answer = max(dp[n-1],dp[n-2])

print(answer)
n = int(input())


INF = int(1e9)

First_answer_dp = [[] for _ in range(n+1)]
Second_answer_dp = [INF] * (n+1) 
Second_answer_dp[1] = 0
First_answer_dp[1] = [1]
for i in range(2,n+1):
    First_answer_dp[i] = First_answer_dp[i-1] + [i]
    Second_answer_dp[i] = Second_answer_dp[i-1] + 1
    if i % 3 == 0:
        if Second_answer_dp[i] > Second_answer_dp[i//3] + 1:
            Second_answer_dp[i] = Second_answer_dp[i//3] + 1
            First_answer_dp[i] = First_answer_dp[i//3] + [i]
    if i % 2 == 0:
        if Second_answer_dp[i] > Second_answer_dp[i//2] + 1:
            Second_answer_dp[i] = Second_answer_dp[i//2] + 1
            First_answer_dp[i] = First_answer_dp[i//2] + [i]

First_answer_dp[n].reverse()

print(Second_answer_dp[n])

for i in First_answer_dp[n]:
    print(i,end=" ")
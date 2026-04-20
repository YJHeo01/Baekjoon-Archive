n = int(input())
dp = [[0]*2 for _ in range(n+1)]
five,five_ = 0,0
two,two_ = 0,0

answer = 0
for i in range(1,n+1):
    tmp = i
    if i % 5 == 0:
        tmp = tmp // 5
        five_ += 1
    if i % 2 == 0:
        tmp = tmp // 2
        two_ +=1
    
    dp[i][0] = dp[tmp][0] + five_
    dp[i][1] = dp[tmp][1] + two_
    

    five += dp[i][0]
    two += dp[i][1]

    five_,two_ = 0,0

answer =  min(two,five)

if n == 0:
    answer = 1

print(answer)
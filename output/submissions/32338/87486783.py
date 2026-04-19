t,n = map(int,input().split())

dp = [[-1]*(n+1) for _ in range(2*t + 1)]

max_johwa, min_johwa = 0,0

dp[t][0] = 0

for _ in range(t):
    m,w,v = map(int,input().split())
    if m == -1:
        for i in range(t+min_johwa,t+max_johwa+1):
            for j in range(n):
                if j + w > n: break
                if dp[i][j] < 0: continue
                dp[i-1][j+w] = max(dp[i-1][j+w],dp[i][j]+v)
        min_johwa -= 1
    else:
        for i in range(t+max_johwa,t+min_johwa-1,-1):
            for j in range(n):
                if j + w > n: break
                if dp[i][j] < 0: continue
                dp[i+1][j+w] = max(dp[i+1][j+w],dp[i][j]+v)
        max_johwa += 1

answer_johwa,answer_kiruk = -t,-1

for i in range(t+min_johwa,t):
    for j in range(n):
        if dp[i][j] >= answer_kiruk:
            answer_johwa = i - t
            answer_kiruk = dp[i][j]
            
for i in range(t+1,t+max_johwa+1):
    for j in range(n):
        if dp[i][j] < answer_kiruk: continue
        if dp[i][j] > answer_kiruk:
            answer_johwa = i - t
            answer_kiruk = dp[i][j]
        else:
            if abs(i-t) <= abs(answer_johwa):
                answer_johwa = i - t

for j in range(n):
    if 2 * dp[t][j] >= answer_kiruk:
        answer_kiruk = 2 * dp[t][j]
        answer_johwa = 0
        
print(answer_johwa,answer_kiruk)
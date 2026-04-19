INF = 40001

n = int(input())

a = list(map(int,input().split()))

dp = [False] * INF

dp[0] = True

for i in a:
    for j in range(INF-1,-1,-1):
        if j - i < 0: break
        if dp[j-i]: dp[j] = True
    
m = int(input())

b = list(map(int,input().split()))

for i in b:
    answer = 'N'
    for j in range(INF):
        if dp[j] == False: continue
        if j*2 + i >= INF: break
        if dp[j*2+i] and dp[j+i]:
            answer = 'Y'
            break
    print(answer,end=" ")
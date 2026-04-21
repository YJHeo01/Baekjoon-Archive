answer = 1

n = int(input())

array = list(map(int,input().split()))

dp = [[0]*5001 for _ in range(n)]

INF = 1000000007

dp[1][1] = 1
dp[1][0] = 1

for i in range(2,n):
    for j in range(5001):
        dp[i][j] = dp[i-1][j]
        if j != 0: dp[i][j] += dp[i-1][j-1]
        if j != 5000: dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= INF

command = []

for i in range(n):
    if array[i] != -1:
        if array[i] > min(i,n-i-1): answer = 0
        command.append((array[i],i))
        
if array[0] == -1:
    command = [(0,0)] + command
    
if array[n-1] == -1:
    command += [(0,n-1)]
    
length = len(command)

for i in range(1,length):
    l_h, l_i = command[i-1]
    r_h, r_i = command[i]
    if l_h > 5000 or r_h > 5000:
        answer = 0
        continue
    answer *= (dp[r_i-l_i][abs(r_h-l_h)])
    answer %= INF
    
print(answer)
s = list(input())

l = len(s)

INF = int(1e9)

dp = [[-INF]*5 for _ in range(l+1)]

for i in range(5):
    dp[0][i] = 0

for i in range(1,l+1):
    dp[i][0] = dp[i-1][0]
    dp[i][4] = max(dp[i-1][4],dp[i-1][3])
    for j in [0,4]:
        if i >= 3 and s[i-2] == '^':
            if s[i-1] == '+' and s[i-3] == '+':
                dp[i][j] += 1
            if s[i-1] == '-' and s[i-3] == '-':
                dp[i][j] -= 1
    for j in [1,2,3]:
        dp[i][j] = dp[i-1][j-1]
        if j == 1 or i <= 3: continue
        dx = 0
        idx = 0
        c = []
        for _ in range(3):
            dx += 1
            while True:
                if dx != j:
                    idx += 1
                    break
                else:
                    dx += 1
            c.append(s[i-dx])
        if c[1] != '^': continue
        if c[0] == c[2]:
            if c[0] == '+':
                dp[i][j] += 1
            if c[0] == '-':
                dp[i][j] -= 1
            

print(max(dp[l]))
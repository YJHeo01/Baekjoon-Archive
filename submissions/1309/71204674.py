n = int(input())

dp0 = [0] * (n+1)
dp1 = [0] * (n+1)

dp0[1] = 1
dp1[1] = 2
for i in range(2,n+1):
    dp0[i] = (dp0[i-1] + dp1[i-1])%9901
    dp1[i] = (2*dp0[i-1] + dp1[i-1])%9901

print((dp0[n]+dp1[n])%9901)
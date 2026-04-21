import sys

input = sys.stdin.readline

n = int(input())

k,c = map(int,input().split())

array = list(map(int,input().split()))

INF = int(1e9)

dp = [0] * (n+1)

for i in range(k-1):
    dp[i+1] = dp[i] + array[i]
    
for i in range(k-1,n):
    dp[i+1] = min(dp[i]+array[i],dp[i-k+1]+c)

print(dp[n])

idx = n

answer = []

while True:
    if idx == 0: break
    if dp[idx-1] + array[idx-1] == dp[idx]:
        idx -= 1
    else:
        idx -= (k-1)
        answer.append(idx)

answer.reverse()

for i in answer:
    print(i)
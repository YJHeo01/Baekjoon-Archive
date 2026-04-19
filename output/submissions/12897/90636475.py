import math

n = int(input())

answer = 0

tmp = 1

INF = 1000000007

visited = [False] * (n+1)


for k in range(1,n+1):
    if math.comb(n,k) >= INF: break
    visited[k] = True
    visited[n-k+1] = True
    
for k in range(1,n+1):
    tmp <<= 1
    tmp %= INF
    if visited[k] == False: continue
    answer += tmp * math.comb(n,k)
    answer %= INF
    
print(answer)
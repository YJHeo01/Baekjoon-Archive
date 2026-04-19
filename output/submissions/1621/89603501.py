from collections import deque

n = int(input())

k,c = map(int,input().split())

array = list(map(int,input().split()))

dp = [0] * (n+1)

for i in range(k-1):
    dp[i+1] = dp[i] + array[i]
    
for i in range(k-1,n):
    dp[i+1] = min(dp[i]+array[i],dp[i-k+1]+c)

print(dp[n])

idx = n

answer = []

queue = deque([n])

visited = [-1] * (n+1)
visited[n] = 0

dx = [-1,-(k-1)]

while queue:
    vx = queue.popleft()
    for i in range(2):
        nx = vx + dx[i]
        if nx < 0 or visited[nx] != -1: continue
        if i == 0 and dp[nx] + array[nx] != dp[vx]: continue
        if i == 1 and dp[nx-1] + c != dp[vx]: continue
        visited[nx] = visited[vx] + 1
        queue.append(nx)

idx = 1

while True:
    if idx + (k-1) > n: break
    if visited[idx+(k-1)] + 1 == visited[idx]:
        print(idx)
        idx += (k-1)
    else:
        idx += 1
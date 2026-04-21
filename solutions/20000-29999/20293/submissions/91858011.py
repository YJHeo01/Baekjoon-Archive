import sys

input = sys.stdin.readline

r,c = map(int,input().split())

n = int(input())

pos = [(1,1,0)]

for i in range(n):
    a,b,z = map(int,input().split())
    pos.append((a,b,z))

pos.append((r,c,0))

pos.sort(key=lambda x:x[0]+x[1])

graph = [[] for _ in range(n+2)]

for i in range(n+2):
    x,y,z = pos[i]
    for j in range(n+2):
        if i == j: continue
        nx,ny,nz = pos[j]
        if nx >= x and ny >= y: graph[i].append(j)

answer = r * c

left, right = 0, answer

dp = [-1] * (n+2)

while left <= right:
    mid = (left+right) // 2
    dp[0] = mid
    for i in range(n+2):
        x,y,z = pos[i]
        if dp[i] < 0: continue
        dp[i] += z
        for j in graph[i]:
            nx,ny,nz = pos[j]
            dp[j] = max(dp[j],dp[i]-abs(nx-x)-abs(ny-y))
    if dp[n+1] != -1:
        answer = mid
        right = mid - 1
        dp = [-1] * (n+2)
    else:
        left = mid + 1

print(answer)
from collections import deque

a, b = map(int,input().split())

dp = [b] * (b+1)

queue = deque([a])

dp[a] = 1
answer = -1
while queue:
    vx = queue.popleft()
    nx = vx * 2
    if nx <= b:
        if dp[nx] > dp[vx] + 1:
            dp[nx] = dp[vx] + 1
            queue.append(nx)
            if nx == b:
                answer = dp[b]
                break
    nx = vx * 10 + 1
    if nx <= b:
        if dp[nx] > dp[vx] + 1:
            dp[nx] = dp[vx] + 1
            queue.append(nx)
            if nx == b:
                answer = dp[b]
                break
print(answer)
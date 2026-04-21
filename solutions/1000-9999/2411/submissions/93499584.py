n,m,a,b = map(int,input().split())

items = [(1,1),(n,m)]

for _ in range(a):
    items.append(tuple(map(int,input().split())))

block = [[False]*(m+1) for _ in range(n+1)]

for _ in range(b):
    x,y = map(int,input().split())
    block[x][y] = True

items.sort()

answer = 1

dp = [[0]*(m+1) for _ in range(n+1)]

dp[1][1] = 1
for i in range(1,a+2):
    x1,y1 = items[i-1]
    x2,y2 = items[i]
    if y2 < y1:
        answer = 0
        continue
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if block[x][y]: continue
            for dx,dy in [(0,1),(1,0)]:
                nx = x + dx
                ny = y + dy
                if nx > x2 or ny > y2 or block[nx][ny]: continue
                dp[nx][ny] += dp[x][y]

print(dp[n][m])
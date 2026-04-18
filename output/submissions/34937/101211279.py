n,m = map(int,input().split())

answer = 1

INF = int(1e9) + 7

for x in range(n):
    for y in range(m):
        for dx,dy in [(0,1),(1,0)]:
            nx = x + dx
            ny = y + dy
            if nx == n or ny == m: continue
            answer *= 3
            answer %= INF

print(answer)
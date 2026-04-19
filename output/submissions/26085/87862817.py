import sys; input = sys.stdin.readline

n,m = map(int,input().split())

possible = False

card = [list(map(int,input().split())) for _ in range(n)]

cnt = [0] * 2

for x in range(n):
    for y in range(m):
        cnt[card[x][y]] += 1
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if card[x][y] == card[nx][ny]: possible = True

if cnt[0] % 2 == 1 or cnt[1] % 2 == 1 or possible == False:
    print(-1)
else:
    print(1)
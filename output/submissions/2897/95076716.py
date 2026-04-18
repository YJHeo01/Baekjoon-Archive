r,c = map(int,input().split())

grid = [list(input()) for _ in range(r)]

answer = [0] * 5

for i in range(1,r):
    for j in range(1,c):
        cnt = 0
        for dx,dy in [(0,0),(0,-1),(-1,0),(-1,-1)]:
            if grid[i+dx][j+dy] == '#':
                cnt = -1
                break
            if grid[i+dx][j+dy] == 'X':
                cnt += 1
        if cnt == -1: continue
        answer[cnt] += 1

for i in answer:
    print(i)
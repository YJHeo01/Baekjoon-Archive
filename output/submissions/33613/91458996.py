from collections import deque

n = int(input())

r,c = map(int,input().split())

pos = set([])

pos.add((r,c))

queue = deque([])

queue.append((r,c))

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

while queue:
    x,y = queue.popleft()
    for i in range(8):
        vx = x + dx[i]
        vy = y + dy[i]
        if vx <= 0 or vy <= 0 or vx > n or vy > n: continue
        for j in range(8):
            nx = vx + dx[j]
            ny = vy + dy[j]
            if nx <= 0 or ny <= 0 or nx > n or ny > n: continue
            if (nx,ny) not in pos:
                pos.add((nx,ny))
                queue.append((nx,ny))

print(len(pos))
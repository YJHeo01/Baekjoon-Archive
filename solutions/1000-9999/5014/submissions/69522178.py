from collections import deque

INF = int(1e10)

f,s,g,u,d = map(int,input().split())

building = [INF] * f

building[s-1] = 0

dx = [u,-d]

queue = deque([s-1])

while queue:
    vx = queue.popleft()
    for i in range(2):
        nx = vx + dx[i]
        if nx < 0 or nx >= f:
            continue
        if building[nx] > building[vx] + 1:
            building[nx] = building[vx] + 1
            queue.append(nx)
            if nx == (g-1):
                break
if building[g-1] == INF:
    print("use the stairs")
else: print(building[g-1])
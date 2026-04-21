import sys, heapq

input = sys.stdin.readline

n = int(input())

graph = [[[]for _ in range(n)] for _ in range(n)]

for i in range(n):
    roads = list(map(int,input().split()))
    for j in range(n-1):
        dist = roads[j]
        graph[i][j].append((i,j+1,dist,0))
        graph[i][j+1].append((i,j,dist,1))
    if i == n-1: continue
    roads = list(map(int,input().split()))
    for j in range(n):
        dist = roads[j]
        graph[i][j].append((i+1,j,dist,2))
        graph[i+1][j].append((i,j,dist,3))

INF = int(1e9)

distance = [[[[INF,INF] for _ in range(4)] for _ in range(n)] for _ in range(n)]

q = []

for i in range(4):
    distance[0][0][i] = [0,0]
    heapq.heappush(q,(0,0,0,0,i))

while q:
    dist, cnt, x, y, dir = heapq.heappop(q)
    if [dist,cnt] != distance[x][y][dir]: continue
    for nx,ny,dd, ndir in graph[x][y]:
        next_cnt = cnt
        next_dist = dist + dd
        if ndir // 2 != dir // 2: next_cnt -= 1
        if distance[nx][ny][ndir][0] < next_dist: continue
        if distance[nx][ny][ndir][0] == next_dist and distance[nx][ny][ndir][1] <= next_cnt: continue
        distance[nx][ny][ndir] = [next_dist,next_cnt]
        heapq.heappush(q,(next_dist,next_cnt,nx,ny,ndir))

min_dist = INF
max_cnt = 0

for i in range(4):
    if distance[n-1][n-1][i][0] < min_dist:
        min_dist = distance[n-1][n-1][i][0]
        max_cnt = distance[n-1][n-1][i][1]
    if distance[n-1][n-1][i][0] == min_dist:
        max_cnt = min(max_cnt,distance[n-1][n-1][i][1])

max_cnt += 1
max_cnt *= -1

print(min_dist,max_cnt)
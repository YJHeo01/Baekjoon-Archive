import sys, heapq

input = sys.stdin.readline

n,k = map(int,input().split())

INF = int(1e9)

arr = [list(map(int,input().split())) for _ in range(n)]

q = []

s, target_x, target_y = map(int,input().split())
target_x -= 1; target_y -= 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0: continue
        heapq.heappush(q,(0,arr[i][j],i,j))

while q:
    dist, idx, x, y = heapq.heappop(q)
    if dist >= s: break
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] != 0: continue
        arr[nx][ny] = idx
        heapq.heappush(q,(dist+1,idx,nx,ny))
        
print(arr[target_x][target_y])
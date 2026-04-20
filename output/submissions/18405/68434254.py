import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int,input().split())

array = []
virus = [deque([]) for _ in range(n+1)]
for i in range(n):
    tmp = list(map(int,input().split()))
    array.append(tmp)
    for j in range(n):
        if tmp[j] != 0:
            virus[tmp[j]].append((i,j))

s,x,y = map(int,input().split())
dx = [0,1,-1,0]
dy = [1,0,0,-1]
while s:
    s -= 1
    for i in range(1,n+1):
        l = len(virus[i])
        for j in range(l):
            v = virus[i].popleft()
            for p in range(4):
                nx, ny = v[0]+dx[p],v[1]+dy[p]
                if nx < 0 or ny < 0 or nx >= n or ny >=n:
                    continue
                if array[nx][ny] == 0:
                    array[nx][ny] = i
                    virus[i].append((nx,ny))
print(array[x-1][y-1])
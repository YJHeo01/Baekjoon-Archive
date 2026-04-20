import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int,input().split())
array = []
virus = [deque([]) for _ in range(k+1)]
for i in range(n):
    tmp = list(map(int,input().split()))
    array.append(tmp)
    for j in range(n):
        if tmp[j] != 0:
            virus[tmp[j]].append((i,j))

s,x,y = map(int,input().split())

def move(nx,ny):
    if nx < 0 or ny < 0 or nx >= n or ny >=n:
        return
    if array[nx][ny] == 0:
        array[nx][ny] = i
        virus[i].append((nx,ny))

while s:
    s -= 1
    for i in range(1,k+1):
        l = len(virus[i])
        for j in range(l):
            v = virus[i].popleft()
            vx,vy = v[0],v[1]
            move(vx,vy+1)
            move(vx,vy-1)
            move(vx+1,vy)
            move(vx-1,vy)
            
print(array[x-1][y-1])
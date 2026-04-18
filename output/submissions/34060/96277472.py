from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

pos = []

rev_pos = dict()

x = 0

last_y = int(1e9) * 2

for i in range(n):
    y = int(input())
    if last_y >= y:
        x += 1
    pos.append((x,y))
    rev_pos[(x,y)] = i
    last_y = y

answer = 0

visited = [False] * n

for i in range(n):
    if visited[i]: continue
    visited[i] = True
    answer += 1
    queue = deque([pos[i]])
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if (nx,ny) in rev_pos:
                j = rev_pos[(nx,ny)]
                if visited[j]: continue
                visited[j] = True
                queue.append((nx,ny))

print(answer)
print(n)
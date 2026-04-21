from collections import deque
import sys

input = sys.stdin.readline

m,n = map(int,input().split())

k = int(input())

bus = []

for _ in range(k):
    b,x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2 and y2 < y1: y1,y2 = y2,y1
    if y1 == y2 and x2 < x1: x1,x2 = x2,x1
    bus.append((x1,y1,x2,y2))
    
sx,sy,dx,dy = map(int,input().split())

visited = [0] * k

queue = deque([])

for i in range(k):
    x1,y1,x2,y2 = bus[i]
    if x1 == x2 and x1 == sx:
        if y1 <= sy and sy <= y2:
            visited[i] = 1
            queue.append(i)
    if y1 == y2 and y1 == sy:
        if x1 <= sx and sx <= x2:
            visited[i] = 1
            queue.append(i)
            

while queue:
    cur = queue.popleft()
    cur_x1,cur_y1,cur_x2,cur_y2 = bus[cur]
    for next in range(k):
        if visited[next] != 0: continue
        next_x1,next_y1,next_x2,next_y2 = bus[next]
        if cur_x1 == cur_x2:
            if next_x1 == next_x2 and next_x1 == cur_x1:
                if (next_y1 <= cur_y2 and cur_y2 <= next_y2) or (cur_y1 <= next_y2 and next_y2 <= cur_y2):
                    visited[next] = visited[cur] + 1
                    queue.append(next)
            if next_y1 == next_y2:
                if next_x1 <= cur_x1 and cur_x1 <= next_x2 and cur_y1 <= next_y1 and next_y1 <= cur_y2:
                    visited[next] = visited[cur] + 1
                    queue.append(next)
        else:
            if next_y1 == next_y2 and next_y1 == cur_y1:
                if (next_x1 <= cur_x2 and cur_x2 <= next_x2) or (cur_x1 <= next_x2 and next_x2 <= cur_x2):
                    visited[next] = visited[cur] + 1
                    queue.append(next)
            else:
                if next_y1 <= cur_y1 and cur_y1 <= next_y2 and cur_x1 <= next_x1 and next_x1 <= cur_x2:
                    visited[next] = visited[cur] + 1
                    queue.append(next)


answer = int(1e9)

for i in range(k):
    x1,y1,x2,y2 = bus[i]
    if x1 == x2 and x1 == dx:
        if y1 <= dy and dy <= y2:
            answer = min(answer,visited[i])
    if y1 == y2 and y1 == dy:
        if x1 <= dx and dx <= x2:
            answer = min(answer,visited[i])
    
print(answer)
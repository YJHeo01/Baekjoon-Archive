from collections import deque

n,k = map(int,input().split())

SIZE = 100001

visited = [SIZE] * SIZE
path = [0] * SIZE

def bfs(visited,path,start):
    visited[start] = 0
    path[start] = -1
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        if vx * 2 < SIZE:
            nx = vx * 2
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                path[nx] = vx
                queue.append(nx)
        if vx + 1< SIZE:
            nx = vx + 1
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                path[nx] = vx
                queue.append(nx)
        if vx != 0:
            nx = vx - 1
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                path[nx] = vx
                queue.append(nx)

bfs(visited,path,n)

first_answer = visited[k]
second_answer = []
second_answer.append(k)
vx = k
while True:
    nx = path[vx]
    if nx == -1:
        break
    second_answer.append(nx)
    vx = nx

print(first_answer)
while True:
    if second_answer == []:
        break
    idx = second_answer.pop()
    print(idx,end=" ")

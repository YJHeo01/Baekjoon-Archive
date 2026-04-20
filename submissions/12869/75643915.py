from collections import deque

n = int(input())

scv = list(map(int,input().split())) + [0] * (3-n)



INF = int(1e9)

visited = [[[INF]*61 for _ in range(61)]for _ in range(61)]

def solution(visited,start):
    queue = deque([start])
    attack_type = [9,3,1]
    visited[start[0]][start[1]][start[2]] = 0
    while queue:
        vx, vy, vz = queue.popleft()
        for i in range(3):
            for j in range(3):
                if i ==j:
                    continue
                for k in range(3):
                    if i == k or j == k:
                        continue
                    nx = vx - attack_type[i]
                    ny = vy - attack_type[j]
                    nz = vz - attack_type[k]
                    if nx < 0:
                        nx = 0
                    if ny < 0:
                        ny = 0
                    if nz < 0:
                        nz = 0
                    if visited[nx][ny][nz] > visited[vx][vy][vz] + 1:
                        visited[nx][ny][nz] = visited[vx][vy][vz] + 1
                        queue.append((nx,ny,nz))

solution(visited,scv)

answer = visited[0][0][0]

print(answer)
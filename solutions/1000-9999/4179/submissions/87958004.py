import sys

R, C = map(int, sys.stdin.readline().split())

laby = []

for i in range(R):
    tmp = list(map(str, sys.stdin.readline().strip()))
    laby.append(tmp)

visited_j = [[0 for i in range(C)] for j in range(R)]
visited_fire = [[0 for i in range(C)] for j in range(R)]

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque()
def BFS():
    global q
    # 지훈이가 행동하고 불이 퍼저야 돼
    while q:
        # print(q)
        x, y, check = q.popleft()
        if check == 'j': # 지훈이
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    return visited_j[x][y]
                if laby[nx][ny] == '#' or visited_fire[nx][ny] != 0 or visited_j[nx][ny] != 0: 
                    # 지훈이는 벽이 아니고 불이 아닌 곳으로 이동 가능 이외 다른 조건 불필요
                    continue
                if visited_fire[x][y] == visited_j[x][y]:
                    # 지훈이가 움직였던 곳(x,y)에 불이 붙었을 경우
                    continue
                visited_j[nx][ny] = visited_j[x][y] + 1
                q.append([nx,ny,'j'])
                '''
                print('j')
                for i in range(R):
                    print(visited_j[i])
                print('fire')
                for i in range(R):
                    print(visited_fire[i])
                '''
        else: # 불
            for dir in range(4): # 불은 네방향으로 퍼지니까
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if laby[nx][ny] == '#' or visited_fire[nx][ny] != 0: 
                    # 불도 벽이 아니고 불이 아닌 곳으로 네방향 이동 가능
                    continue
                visited_fire[nx][ny] = visited_fire[x][y] + 1
                q.append([nx,ny,'fire'])
    return 0


result = 0

for x in range(R):
    for y in range(C):
        if laby[x][y] == 'J':
            q.append([x,y,'j'])
            visited_j[x][y] = 1
        if laby[x][y] == 'F':
            q.appendleft([x,y,'fire']) # 불이 먼저 번져야 지훈이의 이동 경로 체크가 쉬울듯
            visited_fire[x][y] = 1
result = BFS()   

if result == 0:
    print("IMPOSSIBLE")
else:
    print(result)
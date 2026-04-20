from collections import deque

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

room = [[[]for _ in range(n+2)]for _ in range(n+2)]
light_on = [[False]*(n+2) for _ in range(n+2)]
visited = [[False]*(n+2) for _ in range(n+2)]

for _ in range(m):
    x,y,a,b = map(int,input().split())
    room[x][y].append((a,b))

def solution(graph,visited,light_on):
    ret_value = 1
    queue = deque([(1,1)])
    light_on[1][1] = True
    visited[1][1] = True
    dx = [1,0,-1,0] 
    dy = [0,1,0,-1]
    while queue:
        vx,vy = queue.popleft()
        visited[vx][vy] = True
        for a,b in graph[vx][vy]: #스위치로 불 켬
            if light_on[a][b] == False:
                ret_value += 1
                light_on[a][b] = True
            for i in range(4): #스위치로 불 킨 방에 들어갈 수 있는지 테스트
                side_a = a + dx[i]
                side_b = a + dy[i]
                if visited[side_a][side_b] == True:
                    queue.append((a,b))
                    visited[a][b] = True
                    break
        for i in range(4): #현재 있는 방에서 인접한 방으로 이동
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx == 0 or ny == 0 or nx > n or ny > n:
                continue
            if light_on[nx][ny] == True and visited[nx][ny] == False:
                queue.append((nx,ny))
    return ret_value

print(solution(room,visited,light_on))
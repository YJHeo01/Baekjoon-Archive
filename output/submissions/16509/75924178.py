from collections import deque

INF = int(1e9)

r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

visited = [[INF]*9 for _ in range(10)]

def solution(visited,start,end):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    end_x, end_y = end
    move_type = [[-3,-2],[-3,2],[-2,3],[2,3],[3,2],[3,-2],[-2,-3],[2,-3]]
    dx = [[-1,-1,-1],[-1,-1,-1],[0,-1,-1],[0,1,1],[1,1,1],[1,1,1],[0,-1,-1],[0,1,1]]
    dy = [[0,-1,-1],[0,1,1],[1,1,1],[1,1,1],[0,1,1],[0,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + move_type[i][0]
            ny = vy + move_type[i][1]
            move_possible = True
            if nx < 0 or ny < 0 or nx >= 10 or ny >= 9:
                continue
            tmp_x, tmp_y = vx,vy
            for j in range(2):
                tmp_x = tmp_x  + dx[i][j]
                tmp_y = tmp_y + dy[i][j]
                if tmp_x == end_x and tmp_y == end_y:
                    move_possible = False
                    break
            if move_possible == True and visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    
solution(visited,(r1,c1),(r2,c2))

answer = visited[r2][c2]

if answer >= INF:
    answer = -1

print(answer)
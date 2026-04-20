from collections import deque

n,m = map(int,input().split())

graph = [[[]for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    x,y,a,b = map(int,input().split())
    graph[x][y].append((a,b))


light_on = [[False]*(n+1) for _ in range(n+1)]

def check_move_room(visited,point):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = point
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= 0 or ny <= 0 or nx > n or ny > n:
            continue
        if visited[nx][ny] == True:
            return True
    return False


def bfs(graph,visited,light_on):
    queue = deque([(1,1)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    light_on[1][1] = True
    ret_value = 0
    while queue:
        vx,vy = queue.popleft()
        if visited[vx][vy] == False:
            visited[vx][vy] = True
            ret_value += 1
            for switch_on_x,switch_on_y in graph[vx][vy]:
                light_on[switch_on_x][switch_on_y] = True
                if check_move_room(visited,(switch_on_x,switch_on_y)) == True:
                    queue.append((switch_on_x,switch_on_y))
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n:
                continue
            if light_on[nx][ny] == True and visited[nx][ny] == False:
                queue.append((nx,ny))
    return ret_value

visited = [[False]*(n+1) for _ in range(n+1)]

print(bfs(graph,visited,light_on))
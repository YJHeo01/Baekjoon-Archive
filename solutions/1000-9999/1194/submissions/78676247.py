from collections import deque

def main():
    maze = get_maze(n)
    visited = [[[INF]*64 for _ in range(m)]for _ in range(n)]
    start = get_start(maze)
    visited[start[0]][start[1]][0] = 0
    finish = get_finish(maze)
    bfs(maze,visited,start+[0])
    answer = INF
    for x,y in finish:
        answer = min(answer,min(visited[x][y]))
    if answer >= INF: answer = -1
    print(answer)

def get_maze(n):
    maze = []
    for _ in range(n):maze.append(list(input()))
    return maze

def get_start(maze):
    for x in range(n):
        for y in range(m):
            if maze[x][y] == '0':return [x,y]

def get_finish(maze):
    finish = []
    for x in range(n):
        for y in range(m):
            if maze[x][y] == '1':finish.append((x,y))
    return finish

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    door = {'A':1,'B':2,'C':4,'D':8,'E':16,'F':32}
    key = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32}
    while queue:
        vx,vy,state = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            next_state = state
            if nx < 0 or ny < 0 or nx >= n or ny >=m or graph[nx][ny] == '#':continue
            if graph[nx][ny].isupper() == True:
                if state & door[graph[nx][ny]] == False: continue
            elif graph[nx][ny].islower() == True:
                next_state = state | key[graph[nx][ny]]
            if visited[nx][ny][next_state] > visited[vx][vy][state] + 1:
                visited[nx][ny][next_state] = visited[vx][vy][state] + 1
                queue.append((nx,ny,next_state))
                

if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main()
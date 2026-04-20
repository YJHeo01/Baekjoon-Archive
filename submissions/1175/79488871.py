from collections import deque

def main():
    classroom = get_classroom(n)
    start = get_start(classroom)
    target_a, target_b = get_target(classroom)
    distanceStoP = [[[INF]*4 for _ in range(m)]for _ in range(n)]
    bfs_start = []
    for i in range(4):
        bfs_start.append(start+[i])
    bfs(classroom,distanceStoP,bfs_start)
    answer = INF
    for i in range(4):
        distance = [[[INF]*4 for _ in range(m)]for _ in range(n)]
        bfs(classroom,distance,[target_a+[i]])
        answer = min(answer,distanceStoP[target_a[0]][target_a[1]][i]+min(distance[target_b[0]][target_b[1]]))
    for i in range(4):
        distance = [[[INF]*4 for _ in range(m)]for _ in range(n)]
        bfs(classroom,distance,[target_b+[i]])
        answer = min(answer,distanceStoP[target_b[0]][target_b[1]][i]+min(distance[target_a[0]][target_a[1]]))
    if answer >= INF: answer = -1
    print(answer)

def get_classroom(n):
    ret_value = []
    for _ in range(n):
        ret_value.append(list(input()))
    return ret_value

def get_start(classroom):
    for i in range(n):
        for j in range(m):
            if classroom[i][j] == 'S':
                return [i,j]
    return(-1,-1)

def get_target(classroom):
    ret_value = []
    for i in range(n):
        for j in range(m):
            if classroom[i][j] == 'C':
                ret_value.append([i,j])
    return ret_value

def bfs(graph,visited,start):
    queue = deque(start)
    for x,y,d in start:
        visited[x][y][d] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy,last_direction = queue.popleft()
        for i in range(4):
            if i == last_direction:continue
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == '#':continue
            if visited[nx][ny][i] == INF:
                visited[nx][ny][i] = visited[vx][vy][last_direction] + 1
                queue.append((nx,ny,i))
    
if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main() 
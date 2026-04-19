from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    matrix = get_matrix()
    visited = [[[INF]*(k+1)for _ in range(m)]for _ in range(n)]
    bfs(matrix,visited)
    answer = min(visited[n-1][m-1])
    if answer >= INF:
        answer = -1
    print(answer)

def get_matrix():
    matrix = []
    for _ in range(n):
        tmp = list(input())
        for i in range(m):
            tmp[i] = int(tmp[i])
        matrix.append(tmp)
    return matrix

def bfs(graph,visited):
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1
    while queue:
        vx,vy,crash_cnt = queue.popleft()
        point = (vx,vy,crash_cnt)
        if check_night(visited[vx][vy][crash_cnt]): queue += move_at_night(graph,visited,point)
        else: queue += move_at_noon(graph,visited,point)

def check_night(time):
    if time % 2 == 1:
        return False
    return True

def move_at_night(graph,visited,point):
    x, y, crash_cnt = point; meet_block = False
    ret_value = deque([])
    dx = [0,1,0,-1]; dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if exit_map(nx,ny): continue
        if graph[nx][ny] == 1:
            meet_block = True
            continue
        if visited[nx][ny][crash_cnt] > visited[x][y][crash_cnt] + 1:
            visited[nx][ny][crash_cnt] = visited[x][y][crash_cnt] + 1
            ret_value.append((nx,ny,crash_cnt))
    if meet_block == True:
        visited[x][y][crash_cnt] += 1
        ret_value.append((x,y,crash_cnt))
    return ret_value

def move_at_noon(graph,visited,point):
    x, y, crash_cnt = point
    ret_value = deque([])
    dx = [0,1,0,-1]; dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if exit_map(nx,ny): continue
        block = graph[nx][ny]
        if block == 1 and crash_cnt == k:
            continue
        if visited[nx][ny][crash_cnt+block] > visited[x][y][crash_cnt] + 1:
            visited[nx][ny][crash_cnt+block] = visited[x][y][crash_cnt] + 1
            ret_value.append((nx,ny,crash_cnt+block))
    return ret_value

def exit_map(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return True
    return False

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    main()
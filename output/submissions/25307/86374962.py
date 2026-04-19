from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [list(map(int,input().split())) for _ in range(n)]
    start = get_start(graph)
    target = get_target(graph)
    dummy = get_dummy(graph)
    distance = [[INF]*m for _ in range(n)]
    get_shortest_path(graph,distance,dummy,start)
    answer = INF
    for x,y in target:
        answer = min(answer,distance[x][y])
    if answer >= INF: answer = -1
    print(answer)

def get_start(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 4: return (i,j)

def get_target(graph):
    ret_value = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                ret_value.append((i,j))
    return ret_value

def get_dummy(graph):
    ret_value = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 3:
                ret_value.append((i,j))
    return ret_value

def get_shortest_path(graph,distance,dummy,start):
    queue = deque([start])
    distance[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or impossible_move(graph,dummy,(nx,ny)): continue
            if distance[nx][ny] > distance[vx][vy] + 1:
                distance[nx][ny] = distance[vx][vy] + 1
                queue.append((nx,ny))

def impossible_move(graph,dummy,position):
    x,y = position
    if graph[x][y] == 1: return True
    for dummy_x, dummy_y in dummy:
        if abs(x-dummy_x) + abs(y-dummy_y) <= k: return True
    return False

if __name__ == "__main__":
    INF = int(1e9)
    n,m,k = map(int,input().split())
    main()
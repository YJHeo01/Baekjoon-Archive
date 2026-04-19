from collections import deque
import sys

input = sys.stdin.readline

def main():
    global n,m
    n,m,a,b,k = map(int,input().split())
    block = [[False]*(m+1) for _ in range(n+1)]
    for _ in range(k):
        x,y = map(int,input().split())
        block[x][y] = True
    visited = [[-1]*(m+1) for _ in range(n+1)]
    start = list(map(int,input().split()))
    end_x,end_y = map(int,input().split())
    bfs(block,visited,start,a,b)
    print(visited[end_x][end_y])

def bfs(graph,visited,start,a,b):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    ddx_ddy = get_ddx_ddy(a,b)
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx + a - 1 > n or ny + b - 1 > m:continue
            if visited[nx][ny] != -1:continue
            if check_possible_move(graph,ddx_ddy,(nx,ny)) == False:continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

def get_ddx_ddy(a,b):
    ret_value = []
    for i in range(a):
        ret_value.append([i,0])
        ret_value.append([i,b-1])
    for i in range(b):
        ret_value.append([0,i])
        ret_value.append([a-1,i])
    return ret_value

def check_possible_move(graph,dx_dy,start):
    x,y = start
    for dx,dy in dx_dy:
        nx = x + dx
        ny = y + dy
        if graph[nx][ny] == True: return False
    return True

if __name__ == "__main__":
    main()
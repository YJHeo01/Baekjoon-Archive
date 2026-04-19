import sys

input = sys.stdin.readline
sys.setrecursionlimit(5*10**7)
def main():
    maze = [list(input().rstrip()) for _ in range(n)]
    cost = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    finish = [[False]*m for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if finish[i][j]: continue
            answer += move(maze,cost,visited,finish,(i,j))
    print(answer)
    
def move(maze,cost,visited,finish,start):
    dx_dy = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    vx,vy = start
    if vx < 0 or vy < 0 or vx >= n or vy >= m: return 0
    visited[vx][vy] += 1
    if finish[vx][vy]: return 0
    if visited[vx][vy] == 2:
        finish[vx][vy] = True
        return get_value(maze,cost,visited,start)
    dx,dy = dx_dy[maze[vx][vy]]
    nx,ny = vx + dx, vy + dy
    ret_value = move(maze,cost,visited,finish,(nx,ny))
    finish[vx][vy] = True
    return ret_value

def get_value(maze,cost,visited,start):
    vx,vy = start
    dx_dy = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    dx,dy = dx_dy[maze[vx][vy]]
    nx,ny = vx + dx, vy + dy
    if visited[nx][ny] == 2: return cost[vx][vy]
    return min(cost[vx][vy], get_value(maze,cost,visited,(nx,ny)))


if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
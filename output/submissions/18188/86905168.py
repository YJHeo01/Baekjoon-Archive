def main():
    graph = [list(input()) for _ in range(h)]
    global n
    n = int(input())
    disturb = [list(input().split()) for _ in range(n)]
    visited = [[-1]*w for _ in range(h)]
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 'D':
                visited[x][y] = 0
                dfs(graph,visited,(x,y),disturb,"")
                print("NO")
                return

def dfs(graph,visited,start,disturb,movement):
    x,y = start
    move_cnt = visited[x][y]
    if graph[x][y] == 'Z':
        print("YES")
        print(movement)
        exit(0)
    if move_cnt == n: 
        return
    dx_dy = {'W':(-1,0),'A':(0,-1),'S':(1,0),'D':(0,1)}
    for c in disturb[move_cnt]:
        dx,dy = dx_dy[c]
        nx,ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '@': continue
        visited[nx][ny] = visited[x][y] + 1
        dfs(graph,visited,(nx,ny),disturb,movement+c)
        visited[x][y] = move_cnt

if __name__ == "__main__":
    h,w = map(int,input().split())
    main()
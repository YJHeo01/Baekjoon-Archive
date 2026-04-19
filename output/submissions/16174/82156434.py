def main():
    board = [list(map(int,input().split())) for _ in range(n)]
    dfs(board,[[False]*n for _ in range(n)](0,0))
    print("Hing")

def dfs(graph,visited,start):
    x,y = start
    if graph[x][y] == -1:
        print("HaruHaru")
        exit(0)
    dx = [0,graph[x][y]]
    dy = [graph[x][y],0]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n or visited[nx][ny] == True:
            continue
        visited[nx][ny] = True
        dfs(graph,visited,(nx,ny))

if __name__ == "__main__":
    n = int(input())
    main()
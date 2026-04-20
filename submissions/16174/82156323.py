def main():
    board = [list(map(int,input().split())) for _ in range(n)]
    dfs(board,(0,0))
    print("Hing")

def dfs(graph,start):
    x,y = start
    if x >= n or y >= n:
        return
    if graph[x][y] == -1:
        print("HaruHaru")
        exit(0)
    dfs(graph,(x,y+graph[x][y]))
    dfs(graph,(x+graph[x][y],y))

if __name__ == "__main__":
    n = int(input())
    main()
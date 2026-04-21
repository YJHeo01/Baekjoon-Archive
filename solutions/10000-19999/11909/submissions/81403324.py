import sys

input = sys.stdin.readline

def main():
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    dp = [[0]*n for _ in range(n)]
    for i in range(1,n):
        dp[0][i] = move_right(graph,dp,(0,i))
    for i in range(1,n):
        dp[i][0] = move_down(graph,dp,(i,0))
        for j in range(1,n):
            dp[i][j] = min(move_down(graph,dp,(i,j)),move_right(graph,dp,(i,j)))
    print(dp[n-1][n-1])
        
def move_right(graph,dp,point):
    x,y = point
    if graph[x][y-1] <= graph[x][y]:
        return dp[x][y-1] + graph[x][y] - graph[x][y-1] + 1
    return dp[x][y-1]

def move_down(graph,dp,point):
    x,y = point
    if graph[x][y] >= graph[x-1][y]:
        return dp[x-1][y] + graph[x][y] - graph[x-1][y] + 1
    return dp[x-1][y]

if __name__ == "__main__":
    n = int(input())
    main()
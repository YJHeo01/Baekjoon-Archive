import sys

input = sys.stdin.readline

def main():
    k = 1
    while True:
        n = int(input())
        if n == 0:break
        graph = get_graph(n)
        answer = get_answer(graph,n)
        print(k,end=". ")
        print(answer)
        k += 1

def get_graph(n):
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    return graph

def get_answer(graph,n):
    dp = [[0]*3 for _ in range(n)]
    dp[0][0],dp[0][1] = int(1e9), graph[0][1]
    dp[0][2] = dp[0][1] + graph[0][2]
    for i in range(1,n):
        for j in range(3):
            dp[i][j] = dp[i-1][j] + graph[i][j]
            if j != 0: dp[i][j] = min(dp[i][j],dp[i-1][j-1]+graph[i][j])
            if j != 2: dp[i][j] = min(dp[i][j],dp[i-1][j+1]+graph[i][j])
        for j in range(1,3):
            dp[i][j] = min(dp[i][j],dp[i][j-1] + graph[i][j])
    return dp[n-1][1]

if __name__ == "__main__":
    main()
t = int(input())

for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(2):
        graph.append(list(map(int,input().split())))
    dp = [[0]*n for _ in range(2)]
    for i in range(2):
        dp[i][0] = graph[i][0]
    for i in range(1,n):    
        dp[0][i] = max(dp[0][i-1],dp[1][i-1]+graph[0][i])
        dp[1][i] = max(dp[1][i-1],dp[0][i-1]+graph[1][i])
    print(max(dp[0][n-1],dp[1][n-1]))
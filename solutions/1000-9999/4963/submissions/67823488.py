global ice
ice = [] 
global visited 

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M: return 0
    if not visited[x][y]:
        visited[x][y] = True    
        if ice[x][y] == 1:
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y+1)
            dfs(x-1,y-1)
            dfs(x+1,y-1)
            dfs(x-1,y+1)
while(1):
    M, N = map(int,input().split())
    if M == 0 and N == 0:
        break
    ice = []
    visited = [ [False]*M for _ in range(N)]
    for i in range(N):
        row = list(map(int,input().split()))
        ice.append(row)
    cnt = 0
    
    for i in range(0,N):
        for j in range(0,M):
            if ice[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                cnt += 1


    

    print(cnt)
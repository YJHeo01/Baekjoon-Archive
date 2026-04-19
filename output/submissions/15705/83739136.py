def main():
    array = [list(input()) for _ in range(n)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    visited = [[0]*m for _ in range(n)]
    answer = 0
    for x in range(n):
        for y in range(m):
            if array[x][y] != s[0]: continue
            for k in range(8):
                visited[x][y] = 1
                answer = max(answer,dfs(array,visited,(x,y),(dx[k],dy[k])))
            visited[x][y] = 0
    print(answer)

def dfs(array,visited,point,movement):
    x,y = point
    if visited[x][y] == length:
        return 1
    dx, dy = movement
    nx, ny = x + dx, y + dy
    if nx < 0 or ny < 0 or nx >= n or ny >= m or array[nx][ny] != s[visited[x][y]]:
        visited[x][y] = 0
        return 0
    visited[nx][ny] = visited[x][y] + 1
    visited[x][y] = 0
    return dfs(array,visited,(nx,ny),movement)

if __name__ == "__main__":
    s = input()
    length = len(s)
    n,m = map(int,input().split())
    main()
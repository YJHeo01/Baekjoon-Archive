def main():
    n, east, west, north, south = map(int,input().split())
    percent = [east,west,north,south]
    visited = [[False]*(2*n+1) for _ in range(2*n+1)]
    visited[n][n] = 100
    answer = solution(percent,visited,(n,n),n)
    print(answer)

def solution(percent,visited,start,n):
    x,y = start
    if n == 0: return visited[x][y] / 100
    ret_value = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny]: continue
        visited[nx][ny] = percent[i]
        ret_value += solution(percent,visited,(nx,ny),n-1)
        visited[nx][ny] = 0
    return ret_value * visited[x][y]/ 100

if __name__ == "__main__":
    main()
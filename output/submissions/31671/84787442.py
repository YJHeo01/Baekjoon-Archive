from collections import deque

#Algorithm : BFS, DP

def main():
    teacher = [[False]*(2*n+1) for _ in range(n+1)]
    for _ in range(m):
        y,x = map(int,input().split())
        teacher[x][y] = True
    visited = [[[False]*(n+1) for _ in range(2*n+1)] for _ in range(n+1)]
    #방문 배열 3차원 선언 (x,y좌표 + 당시 최대 방문 높이)
    bfs(teacher,visited)
    answer = -1
    for i in range(n+1):
        if visited[0][2*n][i]: answer = i
    print(answer)
    
def bfs(teacher,visited):
    queue = deque([(0,0,0)])
    visited[0][0][0] = True
    dx = [-1,1]
    dy = [1,1]
    while queue:
        vx, vy, cur_max_high = queue.popleft()
        for i in range(2):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or nx > (2*n-ny) or ny > 2 * n or teacher[nx][ny]: continue
            next_max_high = max(cur_max_high,nx)
            if visited[nx][ny][next_max_high] == False:
                visited[nx][ny][next_max_high] = True
                queue.append((nx,ny,next_max_high))
    
if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
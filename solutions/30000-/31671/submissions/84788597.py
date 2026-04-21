from collections import deque
import sys

input = sys.stdin.readline

def main():
    teacher = [[False]*(2*n+1) for _ in range(n+1)]
    for _ in range(m):
        y,x = map(int,input().split())
        teacher[x][y] = True
    max_high = [[-1]*(2*n+1) for _ in range(n+1)]
    bfs(teacher,max_high)
    answer = max_high[0][2*n]
    print(answer)
    
def bfs(teacher,max_high_list):
    queue = deque([(0,0)])
    max_high_list[0][0] = 0
    dx = [1,-1]
    dy = [1,1]
    while queue:
        vx, vy = queue.popleft()
        for i in range(2):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or nx > (2*n-ny) or ny > 2 * n or teacher[nx][ny]: continue
            if max(nx,max_high_list[vx][vy]) > max_high_list[nx][ny]:
                max_high_list[nx][ny] = max(nx,max_high_list[vx][vy])
                queue.append((nx,ny))

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
import sys, heapq

input = sys.stdin.readline

def main():
    teacher = [[False]*(2*n+1) for _ in range(n+1)]
    for _ in range(m):
        y,x = map(int,input().split())
        teacher[x][y] = True
    max_high = [[-1]*(2*n+1) for _ in range(n+1)]
    dijkstra(teacher,max_high)
    answer = max_high[0][2*n]
    print(answer)
    
def dijkstra(teacher,max_high_list):
    q = []
    heapq.heappush(q,(0,0,0))
    max_high_list[0][0] = 0
    dx = [-1,1]
    dy = [1,1]
    while q:
        cur_max_high, vx, vy, = heapq.heappop(q)
        cur_max_high *= -1
        if max_high_list[vx][vy] > cur_max_high: continue
        for i in range(2):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or nx > (2*n-ny) or ny > 2 * n or teacher[nx][ny]: continue
            next_max_high = max(cur_max_high,nx)
            if next_max_high > max_high_list[nx][ny]:
                max_high_list[nx][ny] = next_max_high
                heapq.heappush(q,(-next_max_high,nx,ny))

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
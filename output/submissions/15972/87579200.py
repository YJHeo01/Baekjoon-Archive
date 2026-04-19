import sys, heapq

input = sys.stdin.readline

def main():
    row_block = [list(map(int,input().split())) for _ in range(n+1)]
    column_block = [list(map(int,input().split())) for _ in range(n)]
    water = [[h]*m for _ in range(n)]
    solution(row_block,column_block,water)
    answer = 0
    for i in range(n):
        for j in range(m):
            answer += water[i][j]
    print(answer)

def solution(row_block,column_block,water):
    q = []
    for i in range(m):
        if row_block[0][i] != -1 and water[0][i] > row_block[0][i]:
            water[0][i] = row_block[0][i]
            heapq.heappush(q,(water[0][i],0,i))
        if row_block[n][i] != -1 and water[n-1][i] > row_block[n][i]:
            water[n-1][i] = row_block[n][i]
            heapq.heappush(q,(water[n-1][i],n-1,i))
    
    for i in range(n):
        if column_block[i][0] != -1 and water[i][0] > column_block[i][0]:
            water[i][0] = column_block[i][0]
            heapq.heappush(q,(water[i][0],i,0))
        if column_block[i][m] != -1 and water[i][m-1] > column_block[i][m]:
            water[i][m-1] = column_block[i][m]
            heapq.heappush(q,(water[i][m-1],i,m-1))
    #print_water(water)
    
    visited = [[False]*m for _ in range(n)]
    while q:
        high, vx, vy = heapq.heappop(q)
        visited[vx][vy] = True
        if high > water[vx][vy]: continue
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = vx + dx
            ny = vy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]: continue
            if dy == 0:
                if dx == 1:
                    block_x, block_y = nx,ny
                else:
                    block_x, block_y = vx,vy
                hole_high = row_block[block_x][block_y]
            else:
                if dy == 1:
                    block_x, block_y = nx,ny
                else:
                    block_x, block_y = vx,vy
                hole_high = column_block[block_x][block_y]
            if hole_high == -1 or hole_high > water[nx][ny] or water[vx][vy] >= water[nx][ny]: continue
            next_high = max(water[vx][vy], hole_high)
            if next_high >= water[nx][ny]: continue
            visited[nx][ny] = True
            water[nx][ny] = next_high
            heapq.heappush(q,(next_high,nx,ny))

if __name__ == "__main__":
    n,m,h = map(int,input().split())
    main()
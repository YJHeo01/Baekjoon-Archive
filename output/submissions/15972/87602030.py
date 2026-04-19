import sys, heapq

input = sys.stdin.readline

def main():
    row_block = [list(map(int,input().split())) for _ in range(n+1)]
    column_block = [list(map(int,input().split())) for _ in range(n)]
    hole = [[[h]*4 for _ in range(m)] for _ in range(n)]
    min_high = [[h]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            hole[i][j][0] = row_block[i][j]
            hole[i][j][1] = row_block[i+1][j]
            hole[i][j][2] = column_block[i][j]
            hole[i][j][3] = column_block[i][j+1]
    pos = [[] for _ in range(h)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if hole[i][j][k] == -1: continue
                min_high[i][j] = min(min_high[i][j],hole[i][j][k])
            if min_high[i][j] != h:
                pos[min_high[i][j]].append((i,j))
    water = [[h]*m for _ in range(n)]
    solution(hole,water,min_high,pos)
    answer = 0
    for i in range(n):
        for j in range(m):
            answer += water[i][j]
    print(answer)

def solution(hole,water,min_high,pos):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(h):
        q = []
        for x,y in pos[i]:
            if water[x][y] != h: continue
            for k in range(4):
                if hole[x][y][k] < 0: continue
                nx,ny = x + dx[k], y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    water[x][y] = min(water[x][y],hole[x][y][k])
                else:
                    water[x][y] = min(water[x][y],max(water[nx][ny],hole[x][y][k]))
            if water[x][y] != h:
                heapq.heappush(q,(water[x][y],x,y))
        while q:
            high, vx, vy = heapq.heappop(q)
            if high > water[vx][vy]: continue
            for k in range(4):
                if hole[vx][vy][k] == -1: continue
                nx = vx + dx[k]
                ny = vy + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or min_high[nx][ny] > i:continue
                next_high = max(high,hole[vx][vy][k])
                if water[nx][ny] > next_high:
                    water[nx][ny] = next_high
                    heapq.heappush(q,(next_high,nx,ny))
def print_water(water):
    for i in range(n):
        for j in range(m):
            print(water[i][j],end=" ")
        print()
    print()    
            
if __name__ == "__main__":
    n,m,h = map(int,input().split())
    main()
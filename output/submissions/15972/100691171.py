from collections import deque
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
    #print_water(water)
    print(answer)

def solution(row_block,column_block,water):
    start = [deque([]) for _ in range(h+1)]
    for i in range(m):
        if row_block[0][i] != -1 and water[0][i] > row_block[0][i]:
            start[row_block[0][i]].append((0,i))
            water[0][i] = row_block[0][i]
        if row_block[n][i] != -1 and water[n-1][i] > row_block[n][i]:
            start[row_block[n][i]].append((n-1,i))
            water[n-1][i] = row_block[n][i]
    
    for i in range(n):
        if column_block[i][0] != -1 and water[i][0] > column_block[i][0]:
            water[i][0] = column_block[i][0]
            start[column_block[i][0]].append((i,0))
        if column_block[i][m] != -1 and water[i][m-1] > column_block[i][m]:
            water[i][m-1] = column_block[i][m]
            start[column_block[i][m]].append((i,m-1))
    
    queue = deque([])
    for i in range(h+1):
        next_queue = deque([])
        queue += start[i]
        while queue:
            vx,vy = queue.popleft()
            next_queue_target = False
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = vx + dx
                ny = vy + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
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
                if hole_high == -1 or water[nx][ny] <= i: continue
                if hole_high <= i:
                    water[nx][ny] = i
                    queue.append((nx,ny))
                else:
                    next_queue_target = True
                if next_queue_target: next_queue.append((vx,vy))
        queue = next_queue

def print_water(water):
    for i in range(n):
        for j in range(m):
            print(water[i][j],end=" ")
        print()
    print()    
            
if __name__ == "__main__":
    n,m,h = map(int,input().split())
    main()
import heapq

def main():

    town = [list(input()) for _ in range(n)]

    high = [list(map(int,input().split())) for _ in range(n)]

    start = get_start(town)

    target = get_target(town)

    max_high, min_high = [[INF]*n for _ in range(n)], [[0]*n for _ in range(n)]
    
    start_x, start_y = start
    
    set_max_high(high,max_high,start)
    set_min_high(high,min_high,start)

    target_max_high, target_min_high = 0, INF
    for x,y in target:
        target_max_high = max(target_max_high,max_high[x][y])
        target_min_high = min(target_min_high,min_high[x][y])

    print(target_max_high-target_min_high)

def get_start(town):
    for x in range(n):
        for y in range(n):
            if town[x][y] == 'P':
                return (x,y)

def get_target(town):
    target = []
    for x in range(n):
        for y in range(n):
            if town[x][y] == 'K':
                target.append((x,y))
    return target

def set_max_high(high,max_high,start):
    q = []
    heapq.heappush(q,(high[start[0]][start[1]],start[0],start[1]))
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    while q:
        cur_max,vx,vy = heapq.heappop(q)
        if cur_max > max_high[vx][vy]: continue
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            next_max = max(cur_max,high[nx][ny])
            if max_high[nx][ny] > next_max:
                max_high[nx][ny] = next_max
                heapq.heappush(q,(next_max,nx,ny))

def set_min_high(high,min_high,start):
    q = []
    heapq.heappush(q,(-high[start[0]][start[1]],start[0],start[1]))
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    while q:
        cur_min,vx,vy = heapq.heappop(q)
        cur_min *= -1
        if cur_min < min_high[vx][vy]: continue
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            next_min = min(cur_min,high[nx][ny])
            if min_high[nx][ny] < next_min:
                min_high[nx][ny] = next_min
                heapq.heappush(q,(-next_min,nx,ny))

if __name__ == "__main__":
    INF = 1000000 + 1
    n = int(input())
    main()

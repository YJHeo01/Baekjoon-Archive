from collections import deque

def main():

    town = [list(input()) for _ in range(n)]

    high = [list(map(int,input().split())) for _ in range(n)]

    start = get_start(town)

    target = get_target(town)

    max_high, min_high = INF, 0

    left, right = high[start[0]][start[1]], INF

    while left <= right:
        mid = (left+right) // 2
        visited = [[False]*n for _ in range(n)]
        max_high_bfs(high,visited,start,mid)
        if check_success(visited,target):
            max_high = mid
            right = mid - 1
        else:
            left = mid + 1

    left, right = 0, high[start[0]][start[1]]

    while left <= right:
        mid = (left+right)
        visited = [[False]*n for _ in range(n)]
        min_high_bfs(high,visited,start,mid)
        if check_success(visited,target):
            min_high = mid
            left = mid + 1
        else:
            right = mid - 1
    print(max_high-min_high)

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

def max_high_bfs(high,visited,start,target):
    queue = deque([start])
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if visited[nx][ny] == False and high[nx][ny] <= target:
                visited[nx][ny] = True
                queue.append((nx,ny))

def min_high_bfs(high,visited,start,target):
    queue = deque([start])
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    while queue:
        vx,vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if visited[nx][ny] == False and high[nx][ny] >= target:
                visited[nx][ny] = True
                queue.append((nx,ny))
    
def check_success(visited,target):
    for x,y in target:
        if visited[x][y] == False:
            return False
    return True

if __name__ == "__main__":
    INF = 1000000
    n = int(input())
    main()
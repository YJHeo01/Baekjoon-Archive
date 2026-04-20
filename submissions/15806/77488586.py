from collections import deque
import sys

input = sys.stdin.readline

def main():
    start = get_start()
    visited = [[[False]*(n+1) for _ in range(n+1)]for _ in range(2)]
    move_mold(visited,start)
    yes = get_answer(visited)
    if yes == True:
        print("YES")
    else:
        print("NO")

def get_start():
    start = []
    for _ in range(m):
        start.append(list(map(int,input().split())) + [0])
    return start

def move_mold(visited,start):
    queue = deque(start)
    dx = [2,2,1,1,-1,-1,-2,-2]
    dy = [1,-1,2,-2,2,-2,1,-1]
    for x,y,z in start:
        visited[z%2][x][y] = True
    while queue:
        vx, vy, time = queue.popleft()
        if time == t:
            continue
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n:
                continue
            if visited[(time+1)%2][nx][ny] == True:
                continue
            visited[(time+1)%2][nx][ny] = True
            queue.append((nx,ny,time+1))

def get_answer(visited):
    yes = False
    for _ in range(k):
        a,b = map(int,input().split())
        if visited[t%2][a][b] == True:
            yes = True
            break
    return yes

if __name__ == "__main__":
    n,m,k,t = map(int,input().split())
    if n < 3:
        exit(0)
    main()
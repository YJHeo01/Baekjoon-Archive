from collections import deque

def main():
    a,b,n,m = map(int,input().split())
    visited = [INF] * INF      
    visited = bfs([a,b],visited,n)
    answer = visited[m]
    print(answer)

def bfs(sky_kong,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        queue += warp(sky_kong,visited,vx)
        queue += jump(sky_kong,visited,vx)    
    return visited

def jump(sky_kong,visited,vx):
    a,b = sky_kong
    dx = [a,b,1,-1,-a,-b]
    queue = deque([])
    for i in range(6):
        nx = vx + dx[i]
        if nx < 0 or nx >= INF or visited[nx] <= visited[vx] + 1: continue
        visited[nx] = visited[vx] + 1
        queue.append(nx)
    return queue

def warp(sky_kong,visited,vx):
    queue = deque([])
    for dx in sky_kong:
        nx = vx * dx
        if nx >= INF or visited[nx] <= visited[vx] + 1: continue
        visited[nx] = visited[vx] + 1
        queue.append(nx)
    return queue

if __name__ == "__main__":
    INF = 100001
    main()
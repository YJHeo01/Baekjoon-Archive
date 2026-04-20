from collections import deque

INF = int(1e9)

n, k = map(int,input().split())

def bfs(start,dest):
    queue = deque([(start,0)])
    second = 0
    bro_x = dest
    bro_information = []
    while bro_x <= 500000:
        bro_information.append(bro_x)
        second += 1
        bro_x += second      
    dx = [1,-1]
    while queue:
        vx, sb_second = queue.popleft()
        if sb_second >= second:
            continue
        if bro_information[sb_second] == vx:
            return sb_second
        for i in range(2):
            nx = vx + dx[i]
            if nx < 0 or nx > 500000:
                continue
            queue.append((nx,sb_second+1))
        nx = vx * 2
        if nx > 500000:
            continue
        queue.append((nx,sb_second+1))
    return -1
print(bfs(n,k))
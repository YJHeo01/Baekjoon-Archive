from collections import deque

INF = int(1e9)

n, k = map(int,input().split())

def bfs(start,dest):
    if start == dest:
        return 0
    queue = deque([(start,0)])
    second = 0
    bro_x = dest
    dx = [1,-1]
    while 1:
        second += 1
        bro_x += second
        if bro_x > 500000:
            return -1
        while queue[0][1] == second-1:
            vx, sb_second = queue.popleft()
            for i in range(2):
                nx = vx + dx[i]
                if nx < 0 or nx > 500000:
                    continue
                if nx == bro_x:
                    return second
                queue.append((nx,sb_second+1))
            nx = vx * 2
            if nx > 500000:
                continue
            if nx == bro_x:
                return second
            queue.append((nx,sb_second+1))

print(bfs(n,k))
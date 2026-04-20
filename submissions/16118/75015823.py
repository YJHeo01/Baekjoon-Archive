from collections import deque
import sys,heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,d = map(int,input().split())
    graph[a].append((b,d*2))
    graph[b].append((a,d*2))

INF = int(2e9)

fox_time = [INF] * (n+1)
wolf_time = [[INF]*2 for _ in range(n+1)]

def move_fox(graph,time_list):
    q = []
    heapq.heappush(q,(0,1))
    time_list[1] = 0
    while q:
        time, vx = heapq.heappop(q)
        if time > time_list[vx]:
            continue
        for nx, nt in graph[vx]:
            if time_list[nx] > time_list[vx] + nt:
                time_list[nx] = time_list[vx] + nt
                heapq.heappush(q,(time_list[nx],nx))

def get_next_mode(mode):
    if mode == 1:
        return 0
    else:
        return 1

def move_wolf(graph,time_list):
    queue = deque([(1,1)])
    time_list[1][1] = 0
    time_list[1][0] = 0
    while queue:
        vx, speed_mode = queue.popleft()
        next_mode = get_next_mode(speed_mode)
        for nx,length in graph[vx]:
            if speed_mode == 1:
                nt = length // 2
            else:
                nt = length * 2
            if time_list[nx][next_mode] > time_list[vx][speed_mode] + nt:
                time_list[nx][next_mode] = time_list[vx][speed_mode] + nt
                queue.append((nx,next_mode))
    ret_value = [0] * (n+1)
    for i in range(n+1):
        ret_value[i] = min(time_list[i])
    return ret_value

move_fox(graph,fox_time)
wolf_time = move_wolf(graph,wolf_time)

answer = 0

for i in range(n+1):
    if wolf_time[i] > fox_time[i]:
        answer += 1

print(answer)
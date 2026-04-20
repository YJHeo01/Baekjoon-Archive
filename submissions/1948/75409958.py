from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

indegree = [0] * (n+1)
dest_time = [0] * (n+1)
slowest_path_road_cnt = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    indegree[b] += 1
    graph[a].append((b,c))

start,end = map(int,input().split())

queue = deque([start])

while queue: #만나는 시간
    vx = queue.popleft()
    for nx, time in graph[vx]:
        if dest_time[vx] + time > dest_time[nx]:
            dest_time[nx] = dest_time[vx] + time
            slowest_path_road_cnt[nx] = slowest_path_road_cnt[vx] + 1
        elif dest_time[vx] + time == dest_time[nx]:
            slowest_path_road_cnt[nx]
        indegree[nx] -= 1
        if indegree[nx] == 0:
            queue.append(nx)
print(dest_time[end])

def solution(graph,visited_road,dest_time,start):
    if graph[start] == []:
        return 1
    ret_value = 0
    one = False
    for nx, time in graph[start]:
        if dest_time[nx] == dest_time[start] + time:
            if visited_road[nx][start] == False:
                tmp = solution(graph,visited_road,dest_time,nx)
                if tmp > 0:
                    ret_value += tmp
                    visited_road[nx][start] = True
                    visited_road[start][nx] = True
            else:
                one = True
    if ret_value > 0:
        ret_value += 1
    if ret_value == 0 and one == True:
        ret_value = 1
    return ret_value
visited_road = [[False]*(n+1) for _ in range(n+1)]
second_line_answer = solution(graph,visited_road,dest_time,start) - 1
print(second_line_answer)
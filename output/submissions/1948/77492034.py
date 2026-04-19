from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    indegree = [0] * (n+1)
    graph = get_graph_indegree(indegree)
    slowest_path_road_cnt = [0] * (n+1)
    start,end = map(int,input().split())
    dest_time = get_dest_time(graph,indegree,slowest_path_road_cnt,start)
    time = dest_time[end]
    visited_road = [[False]*(n+1) for _ in range(n+1)]
    road_cnt = get_road_cnt(graph,visited_road,dest_time,start) - 1
    print(time)
    print(road_cnt)

def get_graph_indegree(indegree):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        indegree[b] += 1
        graph[a].append((b,c))
    return graph

def get_dest_time(graph,indegree,slowest_path_road_cnt,start):
    queue = deque([start])
    dest_time = [0] * (n+1)
    while queue:
        vx = queue.popleft()
        for nx, time in graph[vx]:
            if dest_time[vx] + time > dest_time[nx]:
                dest_time[nx] = dest_time[vx] + time
                slowest_path_road_cnt[nx] = slowest_path_road_cnt[vx] + 1
            indegree[nx] -= 1
            if indegree[nx] == 0:
                queue.append(nx)
    return dest_time

def get_road_cnt(graph,visited_road,dest_time,start):
    if graph[start] == []:
        return 1
    ret_value = 0
    one = False
    for nx, time in graph[start]:
        if dest_time[nx] == dest_time[start] + time:
            if visited_road[nx][start] == False:
                tmp = get_road_cnt(graph,visited_road,dest_time,nx)
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

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    main()
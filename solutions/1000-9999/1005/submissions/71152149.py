#https://github.com/YJHeo01]

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

INF = int(1e9)

def dfs(building):
    if reverse_tech_tree[building] == []:
        return building
    return dfs(reverse_tech_tree[building][0])

    
def search_start_build(building):
    return dfs(building)

def bfs(graph,visited,start,time):
    queue = deque([start])
    while queue:
        building = queue.popleft()
        for next_building in graph[building]:
            if visited[next_building] < visited[building] + time[next_building]:
                visited[next_building] = visited[building] + time[next_building]
                queue.append(next_building)

def search_answer(tech_tree,time_list,start,time):
    bfs(tech_tree,time_list,start,time)

for _ in range(t):
    n,k = map(int,input().split())
    build_time = [0] + list(map(int,input().split()))
    tech_tree = [[] for _ in range(n+1)]
    reverse_tech_tree = [[] for _ in range(n+1)]
    for _ in range(k):
        pre_building, building = map(int,input().split())
        tech_tree[pre_building].append(building)
        reverse_tech_tree[building].append(pre_building)
    destination_building = int(input())
    start_build = search_start_build(destination_building)
    dp = [0] * (n+1)
    dp[start_build] = build_time[start_build]
    search_answer(tech_tree,dp,start_build,build_time)
    print(dp[destination_building])
from collections import deque
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    indegree[a] += 1
    indegree[b] += 1

cycle = [False] * (n+1)
visited_edge = [[False]*(n+1) for _ in range(n+1)]
visited_node = [False] * (n+1)

def find_cycle(graph,visited_node,visited_edge,cycle,vx):
    visited_node[vx] = True
    for nx in graph[vx]:
        if visited_edge[vx][nx] == True:
            continue
        visited_edge[vx][nx] = True
        visited_edge[nx][vx] = True
        if visited_node[nx] == True:
            cycle[nx] = True
            cycle[vx] = True
        else:
            tmp = find_cycle(graph,visited_node,visited_edge,cycle,nx)
            if tmp == True:
                if cycle[vx] == True:
                    return False
                else:
                    cycle[vx] = True
                    break
    return cycle[vx]

find_cycle(graph,visited_node,visited_edge,cycle,1)

start = []

for i in range(1,n+1):
    if indegree[i] == 1:
        start.append(i)

INF = int(1e9)

distance = [INF] * (n+1)

def get_distance(graph,distance,cycle):
    queue = deque([])
    for i in range(1,n+1):
        if cycle[i] == True:
            queue.append(i)
            distance[i] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if distance[nx] > distance[vx] + 1:
                distance[nx] = distance[vx] + 1
                queue.append(nx)

get_distance(graph,distance,cycle)

for i in range(1,n+1):
    print(distance[i],end=" ")        
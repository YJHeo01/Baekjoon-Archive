import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def find_cycle(graph,visited,cycle,vx):#순환선 찾는 함수
    for nx in graph[vx]:
        if visited[nx] == INF:
            visited[nx] = visited[vx] + 1
            tmp = find_cycle(graph,visited,cycle,nx)
            if tmp == True:
                if cycle[vx] == True:
                    return False
                else:
                    cycle[vx] = True
            else:
                cycle[vx] = cycle[vx] or tmp
        elif visited[nx] == visited[vx] - 1:
            continue
        else:
            cycle[nx] = True
            cycle[vx] = True
            return True
    return cycle[vx]

visited = [INF] * (n+1)
visited[1] = 1
cycle = [False] * (n+1)
find_cycle(graph,visited,cycle,1)

cycle_distance = [INF] * (n+1)
visited = [False] * (n+1)

def find_distance(graph,visited,cycle_distance,vx):
    visited[vx] = True
    for nx in graph[vx]:
        if visited[nx] == True:
            cycle_distance[vx] = min(cycle_distance[vx],cycle_distance[nx]+1)
        elif cycle_distance[nx] == 0:
            cycle_distance[vx] = 1
            break
        else:
            cycle_distance[vx] = find_distance(graph,visited,cycle_distance,nx) + 1
    return cycle_distance[vx]

for i in range(1,n+1):
    if cycle[i] == True:
        cycle_distance[i] = 0

for i in range(1,n+1):
    if len(graph[i]) == 1:
        find_distance(graph,visited,cycle_distance,i)

for i in range(1,n+1):
    print(cycle_distance[i],end=" ")
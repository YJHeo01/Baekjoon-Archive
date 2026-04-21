from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

def topology_sort(graph,reverse_graph,indegree,strahler,start):
    queue = deque(start)
    while queue:
        vx = queue.popleft()
        if reverse_graph[vx] != []:
            last_max_strahler = 0
            cnt = 0
            for nx in reverse_graph[vx]:
                if strahler[nx] > last_max_strahler:
                    last_max_strahler = strahler[nx]
                    cnt = 1
                elif strahler[nx] == last_max_strahler:
                    cnt += 1
                else:
                    continue
            strahler[vx] = last_max_strahler
            if cnt >= 2:
                strahler[vx] += 1
        for nx in graph[vx]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                queue.append(nx)

answer = []

for _ in range(t):
    k,m,p = map(int,input().split())
    indegree = [0] * (m+1)
    graph = [[] for _ in range(m+1)]
    reverse_graph = [[] for _ in range(m+1)]
    for _ in range(p):
        a,b = map(int,input().split())
        graph[a].append(b)
        reverse_graph[b].append(a)
        indegree[b] += 1
    strahler = [0] * (m+1)
    start = []
    
    for i in range(1,m+1):
        if indegree[i] == 0:
            start.append(i)
            strahler[i] = 1
    
    topology_sort(graph,reverse_graph,indegree,strahler,start)
    answer.append((k,strahler[m]))

answer.sort()

for idx, num in answer:
    print(idx,num)
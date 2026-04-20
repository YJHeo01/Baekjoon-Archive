import sys

input = sys.stdin.readline

from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def toplogy_sort():
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in graph[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

toplogy_sort()
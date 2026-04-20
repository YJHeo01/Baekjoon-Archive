import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    queue = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(queue,i)
    while queue:
        problem = heapq.heappop(queue)
        print(problem,end=" ")
        for i in graph[problem]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(queue,i)

topology_sort()
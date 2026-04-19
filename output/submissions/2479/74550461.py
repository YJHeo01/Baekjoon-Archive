import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())

code = [[]]
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    code.append(list(input()))

def check_hamming_path(code_A,code_B):
    hamming_distance = 0
    for i in range(k):
        if code_A[i] != code_B[i]:
            hamming_distance += 1
        if hamming_distance > 1:
            return False
    return True

for i in range(1,n):
    for j in range(i+1,n+1):
        if check_hamming_path(code[i],code[j]) == True:
            graph[i].append(j)
            graph[j].append(i)

start,end = map(int,input().split())

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] > visited[vx]+1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

INF = int(1e9)

visited = [INF] * (n+1)

bfs(graph,visited,start)

if visited[end] == INF:
    print(-1)
else:
    def dfs(graph,visited,vx):
        ret_value = [vx]
        while True:
            for nx in graph[vx]:
                if visited[nx] == visited[vx] - 1:
                    ret_value.append(nx)
                    if visited[nx] == 0:
                        ret_value.reverse()
                        return ret_value
                    vx = nx
                    break

    answer = dfs(graph,visited,end)
    for i in answer:
        print(i,end=" ")
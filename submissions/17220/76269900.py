from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n)]

start = [True] * n

for _ in range(m):
    a,b = input().split()
    a = ord(a) - ord('A')
    b = ord(b) - ord('A')
    graph[a].append(b)
    start[b] = False

visited = [False] * n

trash_list = list(input().split())

for i in trash_list[1:]:
    idx = ord(i) - ord('A')
    visited[idx] = True

answer = 0

def solution(graph,visited,start):
    queue = deque([start])
    ret_value = 0
    visited[start] = True
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == True:
                continue
            visited[nx] = True
            queue.append(nx)
            ret_value += 1
    return ret_value

for i in range(n):
    if start[i] == False or visited[i] == True:
        continue
    answer += solution(graph,visited,i)

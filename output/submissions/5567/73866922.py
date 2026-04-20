from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

friend_graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    friend_graph[a].append(b)
    friend_graph[b].append(a)

INF = int(1e9)

visited = [INF]*(n+1)

def solution(graph,visited):
    queue = deque([1])
    visited[1] = 0 
    ret_value = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                if visited[nx] <= 2:
                    ret_value += 1
                    queue.append(nx)
    return ret_value

answer = solution(friend_graph,visited)

print(answer)
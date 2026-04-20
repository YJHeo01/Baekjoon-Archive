from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

work_time = [0]

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    work_time.append(tmp[0])
    indegree[i] = tmp[1]
    for j in tmp[2:]:
        graph[j].append(i)

def solution(indegree):
    time_list = [0] * (n+1)
    queue = deque([])
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        time_list[node] += work_time[node]
        for next_node in graph[node]:
            indegree[next_node] -= 1
            time_list[next_node] = max(time_list[next_node],time_list[node])
            if indegree[next_node] == 0:
                queue.append(next_node)
    return max(time_list)

print(solution(indegree))
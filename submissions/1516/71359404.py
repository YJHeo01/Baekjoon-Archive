#https://github.com/YJHeo01
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

next_build_list = [[] for _ in range(n+1)]
pre_build_list = [[] for _ in range(n+1)]

indegree = [0] *(n+1)

answer = [0] * (n+1)

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    answer[i] = tmp[0]
    for pre_build in tmp[1:]:
        if pre_build == -1:
            continue
        indegree[i] += 1
        next_build_list[pre_build].append(i)
        pre_build_list[i].append(pre_build)

def topology_sort(answer):
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        value = queue.popleft()
        for next_build in next_build_list[value]:
            indegree[next_build] -= 1
            if indegree[next_build] == 0:
                queue.append(next_build)
        plus_time = 0
        for i in pre_build_list[value]:
            if answer[i] > plus_time:
                plus_time = answer[i]
        answer[value] += plus_time
            
        
topology_sort(answer)
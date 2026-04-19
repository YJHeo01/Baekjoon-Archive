from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(26)]

max_flow = [[0]*26 for _ in range(26)]
cur_flow = [[0]*26 for _ in range(26)]

for _ in range(n):
    a,b,c = input().split()
    num_a = int(ord(a)-ord('A'))
    num_b = int(ord(b)-ord('A'))
    c = int(c)
    graph[num_a].append(num_b)
    graph[num_b].append(num_a)
    max_flow[num_a][num_b] += c
    max_flow[num_b][num_a] += c


answer = 0

while True:
    prev = [-1] * 26
    queue = deque([0])
    while queue and prev[25] == -1:
        x = queue.popleft()
        for nx in graph[x]:
            if max_flow[x][nx] > cur_flow[x][nx] and prev[nx] == -1:
                queue.append(nx)
                prev[nx] = x
                if nx == 25: break
    if prev[25] == -1: break

    flow = int(1e9)
    x = 25
    while True:
        if x == 0: break
        flow = min(flow,max_flow[prev[x]][x]-cur_flow[prev[x]][x])
        x = prev[x]
    x = 25
    while True:
        if x == 0: break
        cur_flow[prev[x]][x] += flow
        cur_flow[x][prev[x]] -= flow
        x = prev[x]
    answer += flow
    
print(answer)
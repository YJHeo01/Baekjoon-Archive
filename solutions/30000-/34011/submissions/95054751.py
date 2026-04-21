from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

parent = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

prime = [True] * (n+1)

prime_list = [2,3,5,7,11,13,17,19,21,23,29,31]


for i in range(n-1):
    graph[parent[i]].append(i+2)

queue = deque([1])

depth = [-1] * (n+1)

cnt = [0] * (n+1)

depth[1] = 0

while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if depth[nx] != -1: continue
        depth[nx] = depth[x] + 1
        cnt[depth[nx]] += 1
        queue.append(nx)

if n == 2:
    print(1)
    exit(0)

for i in range(2,max(depth)+1):
    for j in prime_list:
        if i % j == 0:
            cnt[j] += cnt[i]

print(max(cnt[2:])+1)
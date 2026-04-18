from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

parent = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

prime = [True] * (n+1)

prime_list = []

for i in range(2,n+1):
    if prime[i] == True:
        prime_list.append(i)
        for j in range(i,n+1,i):
            prime[j] = False

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

for i in range(2,n+1):
    for j in prime_list:
        if i % j == 0 and i != j:
            cnt[j] += cnt[i]

print(max(cnt[2:])+1)
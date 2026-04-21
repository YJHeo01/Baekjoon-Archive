import sys, heapq

input = sys.stdin.readline

num_list = []

q = [1]

exist = set()

for _ in range(5000000):
    x = heapq.heappop(q)
    num_list.append(x)
    for multiple in [2,3]:
        nx = x * multiple + 1
        if nx in exist: continue
        exist.add(nx)
        heapq.heappush(q,nx)

while q:
    num_list.append(heapq.heappop(q))

t = int(input())

for _ in range(t):
    n = int(input())
    print(num_list[n-1])
import sys, heapq

input = sys.stdin.readline

num_list = []

exist = set()

q = [1]

for _ in range(10000000):
    x = heapq.heappop(q)
    num_list.append(x)
    for multiple in [2,3]:
        nx = x * multiple + 1
        if nx not in exist:
            exist.add(nx)
            heapq.heappush(q,nx)

t = int(input())

for _ in range(t):
    n = int(input())
    print(num_list[n-1])
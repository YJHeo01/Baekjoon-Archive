from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

parent = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

prime = [True] * (n+1)

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631]


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
        if i % j == 0 and i != j:
            cnt[j] += cnt[i]

print(max(cnt[2:])+1)
import sys,heapq

input = sys.stdin.readline

n = int(input())

edges = []
connect = [False] * n

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(i+1,n):
        heapq.heappush(edges,(tmp[j],i,j))

answer = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    if connect[a] == True and connect[b] == True:
        continue
    connect[a] = True; connect[b] = True
    answer += cost

print(answer)

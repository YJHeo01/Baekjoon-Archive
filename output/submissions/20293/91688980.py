import sys, heapq

input = sys.stdin.readline

r,c = map(int,input().split())

n = int(input())

charge = [0] * (n+2)

pos = [(1,1)]

for i in range(n):
    a,b,z = map(int,input().split())
    pos.append((a,b))
    charge[i+1] = z

pos.append((r,c))

graph = [[] for _ in range(n+2)]

for i in range(n+2):
    x,y = pos[i]
    for j in range(n+2):
        if i == j: continue
        nx,ny = pos[j]
        if nx >= x and ny >= y: graph[i].append(j)

answer = r * c

left, right = 0, answer

while left <= right:
    mid = (left+right) // 2
    fuel = [-1] * (n+2)
    fuel[0] = mid
    q = []
    heapq.heappush(q,(-mid,0))
    while q:
        f, x = heapq.heappop(q)
        f *= -1
        if fuel[x] > f: continue
        for nx in graph[x]:
            nf = f + (pos[x][0] - pos[nx][0]) + (pos[x][1] - pos[nx][1]) + charge[x]
            if nf > fuel[nx]:
                fuel[nx] = nf
                heapq.heappush(q,(-nf,nx))
    if fuel[n+1] != -1:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
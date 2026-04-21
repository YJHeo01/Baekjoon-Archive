import sys, heapq

input = sys.stdin.readline

n = int(input())

a_list, b_list, c_list, d_list = [],[],[],[]

for _ in range(n):
    a,b,c,d = map(int,input().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(c+d)

INF = int(1e9)

distance = [INF] * (n+1)

def dijkstra(distance):
    q = []
    distance[0] = 0
    heapq.heappush(q,(0,0))
    while q:
        vd, vx = heapq.heappop(q)
        if vd > distance[vx] or vx == n: continue
        nx = vx + 1
        nd = vd + b_list[vx]
        if distance[nx] > nd:
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))
        if vd % d_list[vx] >= c_list[vx]:
            nd = vd - vd % d_list[vx] + d_list[vx] + a_list[vx]
        else:
            nd = vd + a_list[vx]
        if distance[nx] > nd:
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))
            
dijkstra(distance)

answer = distance[n]

print(answer)
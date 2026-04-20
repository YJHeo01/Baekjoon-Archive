import heapq

n,m,l = map(int,input().split())

if n != 0:
    shop = list(map(int,input().split()))
else:
    shop = []

shop.append(l)
shop.append(0)

distance_list = []

shop.sort()

for i in range(1,n+2):
    heapq.heappush(distance_list,shop[i-1]-shop[i])

for _ in range(m):
    tmp = heapq.heappop(distance_list)
    heapq.heappush(distance_list,tmp//2)
    if tmp % 2 == 1:
        heapq.heappush(distance_list,tmp//2 + 1)
    else:
        heapq.heappush(distance_list,tmp//2)

answer = -heapq.heappop(distance_list)

print(answer)
import heapq

n,m = map(int,input().split())

array = sorted(list(map(int,input().split())),reverse=True)

q = []

for i in range(min(m,n)):
    heapq.heappush(q,array[i])

for i in range(m,n):
    heapq.heappush(q,heapq.heappop(q)+array[i])

while True:
    answer = heapq.heappop(q)
    if q == []:
        print(answer)
        break
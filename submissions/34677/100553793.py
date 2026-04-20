import heapq

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

q = []
visited = [False] * n

for i in range(n):
    heapq.heappush(q,(a[i],i))

answer = 0

while q:
    tmp, x = heapq.heappop(q)
    if visited[x]: continue
    for right in range(x,n):
        if b[x] > b[right]: break
        visited[right] = True
    for left in range(x-1,-1,-1):
        if b[x] > b[left]: break
        visited[left] = True
    answer += 1
    
print(answer)
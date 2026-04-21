import heapq

n,x = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

left = 0
right = int(1e18) + 1

target = right

while left <= right:
    mid = (left+right) // 2
    tmp = 0
    for i in range(n):
        if a[i] >= mid: continue
        tmp += (mid-a[i]) // b[i]
        if (mid-a[i]) % b[i] != 0: tmp += 1
    if tmp > x:
        right = mid - 1
    else:
        left = mid + 1
        target = mid
        
  
for i in range(n):
    if a[i] >= target: continue
    x -= ((target-a[i]) // b[i])
    a[i] += ((target-a[i]) // b[i]) * b[i]
    
q = []

for i in range(n):
    heapq.heappush(q,(a[i],i))
    
for _ in range(x):
    value, idx = heapq.heappop(q)
    value += b[idx]
    a[idx] = value
    heapq.heappush(q,(value,idx))
    
print(*a)
    
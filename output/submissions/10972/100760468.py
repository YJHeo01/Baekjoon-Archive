n = int(input())

arr = list(map(int,input().split()))

idx = -1

for i in range(n-1,1,-1):
    if arr[i-1] < arr[i]:
        idx = i
        arr[i-1],arr[i] = arr[i],arr[i-1]
        break

if idx == -1:
    print(-1)
    exit(0)
    
for i in range(idx,n-1):
    if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]

print(*arr)
n = int(input())

arr = list(map(int,input().split()))

idx = -1

for x in range(n-1,0,-1):
    for i in range(x-1,-1,-1):
        if arr[i] < arr[x]:
            idx = i
            arr[x], arr[i] = arr[i], arr[x]
            break
    if idx != -1: break

if idx == -1:
    print(-1)
    exit(0)

for i in range(n-1,idx+1,-1):
    for j in range(idx+1,i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)
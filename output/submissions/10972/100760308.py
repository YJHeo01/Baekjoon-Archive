n = int(input())

arr = list(map(int,input().split()))

minus = True

for i in range(n-1,1,-1):
    if arr[i-1] < arr[i]:
        minus = False
        arr[i-1],arr[i] = arr[i],arr[i-1]
        break

if minus: print(-1)
else: print(*arr)
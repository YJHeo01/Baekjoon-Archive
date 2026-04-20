n,k,t = map(int,input().split())

arr = sorted(list(map(int,input().split())))

left, right = 0,n-1

while left < right:
    if arr[left] + arr[right] < k:
        arr[right] += arr[left]
        t -= arr[left]
        arr[left] = 0
        left += 1
    else:
        t -= (k-arr[right])
        arr[left] -= (k-arr[right])
        arr[right] = k
        right -= 1
        
if t < 0 or arr[left] % k != 0 or arr[right] % k != 0:
    print("NO")
else:
    print("YES")
n,k,t = map(int,input().split())
array = list(map(int,input().split()))
eat = [False] * n
array.sort()
for _ in range(k):
    left, right = 0,n-1
    target = -1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] < t:
            target = mid
            left = mid + 1
        else:
            right = mid - 1
    while True:
        if target == -1 or eat[target] == False: break
        target -= 1
    if target == -1: break
    eat[target] = True
    t += array[target]
print(t)
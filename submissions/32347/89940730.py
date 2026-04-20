n,k = map(int,input().split())

array = list(map(int,input().split()))

left, right = 1, n - 1

answer = n - 1

while left <= right:
    mid = (left+right) // 2
    visited = [False] * (n+1)
    x = n - 1
    cnt = 0
    visited[x] = True
    while True:
        if array[x] == 1:
            x -= mid
        else:
            x += 1
        if x <= 0 or visited[x]: break
        visited[x] = True
    if x <= 0:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(answer)
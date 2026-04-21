n,m = map(int,input().split())
array = list(map(int,input().split()))
answer = min(array) * m
left, right = 1,answer
while left <= right:
    mid = (left+right) // 2
    tmp = 0
    for i in array:
        tmp += mid // i
    if tmp >= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
n,m,l = map(int,input().split())

road = [0] + list(map(int,input().split())) + [l]

road.sort()

left, right = 1,l-1

answer = l

while left <= right:
    mid = (left+right) // 2
    cnt = 0
    for i in range(n+1):
        cnt += ((road[i+1] - road[i] - 1) // mid)
    if cnt <= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
m,n = map(int,input().split())

snacks = list(map(int,input().split()))

if m < n:
    snacks.sort()
    print(snacks[n-m])
else:
    answer = 0
    right = min(snacks)
    left = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for snack in snacks:
            cnt += (snack // mid)
        if cnt >= m:
            answer = max(answer,mid)
            left = mid + 1
        else:
            right = mid -1
    print(answer)
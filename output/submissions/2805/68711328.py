n,m = map(int,input().split())

tree = list(map(int,input().split()))

low = min(tree)
high = max(tree)
answer = 0

while low <= high:
    sum = 0
    mid = (low+high)//2
    for i in tree:
        if i - mid > 0:
            sum += (i-mid)
    if sum == m:
        answer = mid
        break
    elif sum > m:
        answer = max(answer,mid)
        low = mid + 1
    else:
        high = mid - 1
    if low > high:
        break

print(answer)
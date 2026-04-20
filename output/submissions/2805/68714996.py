n,m = map(int,input().split())

tree = list(map(int,input().split()))

low = 1
high = max(tree)
answer = 0

while low <= high:
    sum = 0
    mid = (low+high)//2
    for i in tree:
        if i - mid > 0:
            sum += (i-mid)
    if sum > m:
        answer = max(answer,mid)
        low = mid + 1
    elif sum < m:
        high = mid - 1
    else:
        answer = max(answer,mid)
        break

print(answer)
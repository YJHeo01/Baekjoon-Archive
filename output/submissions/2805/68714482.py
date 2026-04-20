n,m = map(int,input().split())

tree = list(map(int,input().split()))

tree.sort(reverse=True)
low = tree[-1]
high = tree[0]
answer = 0

while low <= high:
    sum = 0
    mid = (low+high)//2
    for i in tree:
        if i - mid > 0:
            sum += (i-mid)
        else:
            break
    if sum >= m:
        answer = max(answer,mid)
        low = mid + 1
    else:
        high = mid - 1

print(answer)
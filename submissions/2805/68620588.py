n,m = map(int,input().split())

tree = list(map(int,input().split()))

low = 0
high = max(tree)
tree.sort(reverse=True)
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
        if answer == mid:
            break
        answer = max(answer,mid)
        low = mid + 1
    else:
        high = mid - 1

print(answer)
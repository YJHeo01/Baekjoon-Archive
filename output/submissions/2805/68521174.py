n,m = map(int,input().split())

tree = list(map(int,input().split()))

low = min(tree)
high = max(tree)
tree.sort(reverse=True)
answer = 0

while(1):
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
        low = mid 
    else:
        high = mid


print(answer)
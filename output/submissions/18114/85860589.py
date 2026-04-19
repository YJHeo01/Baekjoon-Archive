n,c = map(int,input().split())
array = sorted(list(map(int,input().split())))
for i in array:
    if i == c:
        print(1)
        exit(0)
left,right = 0,n-1
while left < right:
    if array[left] + array[right] > c:
        right -= 1
    elif array[left] + array[right] < c:
        left += 1
    else:
        print(1)
        exit(0)

for mid in range(1,n-1):
    left, right = 0,n-1
    while True:
        if left == mid or right == mid:
            break
        tmp = array[left] + array[mid] + array[right]
        if tmp > c:
            right -= 1
        elif tmp < c:
            left += 1
        else:
            print(1)
            exit(0)

print(0)
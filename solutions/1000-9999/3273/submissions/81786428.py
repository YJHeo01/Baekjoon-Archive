left, right = 0, int(input()) - 1
array = sorted(list(map(int,input().split())))
x = int(input())
answer = 0
while left < right:
    if array[left] + array[right] > x:
        right -= 1
    elif array[left] + array[right] < x:
        left += 1
    else:
        answer += 1
        left += 1
        right -= 1
print(answer)
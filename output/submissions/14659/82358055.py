n = int(input())
array = list(map(int,input().split()))
left, right = 0,1
answer = 0
while right < n:
    if array[right] > array[left]:
        answer = max(answer,right-left-1)
        left = right
    else:
        right += 1
answer = max(answer,right-left-1)
print(answer)
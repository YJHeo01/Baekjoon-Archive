n = int(input())

array = list(map(int,input().split()))

answer = n

start = 0
left, right = 0,1
while right < n:
    if array[right] > array[left]:
        answer += (right-start)
        left += 1
        right += 1
    else:
        start = right
        left = start
        right = left + 1

print(answer)
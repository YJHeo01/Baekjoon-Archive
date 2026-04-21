n = int(input())

tmp = list(map(int,input().split()))

arr = [0] * 5

for i in tmp:
    arr[i] += 1

answer = arr[4]

answer += (arr[2]//2)

arr[2] %= 2

if arr[2] == 1 and arr[1] >= 2:
    answer += 1
    arr[1] -= 2
    arr[2] = 0

answer += arr[2]

answer += max(arr[1],arr[3])

print(answer)
n = int(input())

ttmp = list(map(int,input().split()))

arr = [0] * 5

for i in ttmp:
    arr[i] += 1

tmp = min(arr[2],arr[1]//2)

tmp1 = arr[4]

tmp1 += tmp

arr[2] -= tmp
arr[1] -= 2 * tmp

tmp1 += arr[2]

tmp1 += max(arr[1],arr[3])

arr = [0] * 5

for i in ttmp:
    arr[i] += 1

tmp2 = arr[4]

tmp2 += (arr[2]//2)

arr[2] %= 2

if arr[2] == 1 and arr[1] >= 2:
    tmp2 += 1
    arr[1] -= 2
    arr[2] = 0

tmp2 += arr[2]

tmp2 += max(arr[1],arr[3])

print(min(tmp1,tmp2))
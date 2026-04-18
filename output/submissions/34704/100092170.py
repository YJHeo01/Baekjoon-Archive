n = int(input())

tmp = list(map(int,input().split()))

arr = [0] * 5

for i in tmp:
    arr[i] += 1

tmp = min(arr[2],arr[1]//2)

answer = arr[4]

answer += tmp

arr[2] -= tmp
arr[1] -= 2 * tmp

answer += arr[2]

answer += max(arr[1],arr[3])

print(answer)
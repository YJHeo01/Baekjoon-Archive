n = int(input())

arr = list(map(int,input().split()))

answer = 0

for i in range(2,n):
    tmp = min(arr[i],arr[i-1],arr[i-2])
    answer += tmp * 7
    arr[i] -= tmp
    arr[i-1] -= tmp
    arr[i-2] -= tmp

for i in range(1,n):
    tmp = min(arr[i],arr[i-1])
    answer += tmp * 5
    arr[i] -= tmp
    arr[i-1] -= tmp

answer += sum(arr) * 3

print(answer)
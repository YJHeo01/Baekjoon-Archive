import sys

input = sys.stdin.readline

n = int(input())

arr = [input().rstrip() for _ in range(n)]

answer = 0

for i in range(1,n):
    if len(arr[i]) > len(arr[i-1]): continue
    answer += (len(arr[i])-len(arr[i-1]))
    arr[i] += '0' * (len(arr[i])-len(arr[i-1]))
    if int(arr[i]) < int(arr[i-1]):
        arr[i] += '0'
        answer += 1

print(answer)
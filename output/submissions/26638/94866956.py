import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

answer = 0

for i in range(1,n):
    while True:
        if arr[i] > arr[i-1]: break
        answer += 1
        arr[i] *= 10

print(answer)
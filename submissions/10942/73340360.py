import sys

input = sys.stdin.readline

n = int(input())

array = [0] + list(map(int,input().split()))

m = int(input())

for _ in range(m):
    left, right = map(int,input().split())
    answer = 1
    while left <= right:
        if array[left] != array[right]:
            answer = 0
            break
        left += 1
        right -= 1
    print(answer)
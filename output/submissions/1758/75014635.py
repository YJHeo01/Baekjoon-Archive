import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

answer = 0

for i in range(n):
    if array[i] < i:
        break
    answer += array[i]
    answer -= i

print(answer)
import sys
input = sys.stdin.readline
n = int(input())
array = sorted([int(input()) for _ in range(n)])
answer = 0
for i in range(1,n):
    answer += array[i] - array[i-1]
print(answer)
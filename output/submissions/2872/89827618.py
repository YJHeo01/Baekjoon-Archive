import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]

answer = 0

while True:
    tmp = array.pop()
    if tmp == n: break
    answer = max(answer,tmp)

print(answer)
import sys

input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]

visited = [False] * (n+1)

target = n

idx = n-1

answer = 0

while True:
    while True:
        if visited[target] == False or target == 0: break
        target -= 1
    if target == 0: break
    visited[array[idx]] = True
    if array[idx] != target:
        answer += 1
    else:
        target -= 1
    idx -= 1
if answer != 0 and array[0] == 1: answer += 1

print(answer)
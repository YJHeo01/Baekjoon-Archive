import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

answer = 0

while True:
    target = -1
    mount = int(1e9)
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += arr[i][j]
        if tmp == 0: continue
        if tmp < mount:
            mount = tmp
            target = i + n
    for j in range(m):
        tmp = 0
        for i in range(n):
            tmp += arr[i][j]
        if tmp == 0: continue
        if tmp < mount:
            mount = tmp
            target = j
    if target == -1: break
    answer = max(answer,mount)
    if target < n:
        for i in range(n):
            arr[i][target] = 0
    else:
        for j in range(m):
            arr[target-n][j] = 0
    
print(answer)
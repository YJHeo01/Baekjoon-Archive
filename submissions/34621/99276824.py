import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

left, right = 1, 500000 * max(n,m)

answer = right

while left <= right:
    mid = (left+right)// 2
    tmp_a = [[0]*m for _ in range(n)]
    zero_row = [False] * n
    zero_column = [False] * m
    for i in range(n):
        for j in range(m):
            tmp_a[i][j] = arr[i][j]
    while True:
        finish = True
        not_finish = False
        for i in range(n):
            if zero_row[i]: continue
            tmp = 0
            for j in range(m):
                tmp += tmp_a[i][j]
            if tmp <= mid:
                not_finish = True
                zero_row[i] = True
                for j in range(m):
                    tmp_a[i][j] = 0
            else:
                finish = False
        for j in range(m):
            if zero_column[j]: continue
            tmp = 0
            for i in range(n):
                tmp += tmp_a[i][j]
            if tmp <= mid:
                zero_column[j] = True
                not_finish = True
                for i in range(n):
                    tmp_a[i][j] = 0
            else:
                finish = False
        if sum(zero_column) + sum(zero_row) == n + m: break
        if finish or(not_finish==False): break
    if sum(zero_column) + sum(zero_row) == n + m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
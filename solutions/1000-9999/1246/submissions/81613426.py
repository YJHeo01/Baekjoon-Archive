import sys

input = sys.stdin.readline

n,m = map(int,input().split())

array = sorted([int(input()) for _ in range(m)],reverse=True)

answer = 0

price = 0
for i in range(min(n,m)):
    if array[i] * (i+1) > answer:
        price = array[i]
        answer = array[i] * (i+1)

print(price,answer)
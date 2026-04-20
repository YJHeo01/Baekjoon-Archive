import sys

input = sys.stdin.readline

n,d,k,c = map(int,input().split())

belt = []

answer = 0

for _ in range(n):
    belt.append(int(input()))

for left in range(n):
    select = [False] * (d+1)
    tmp = 0
    for i in range(k):
        idx = (left + i) % n
        if select[belt[idx]] == False:
            select[belt[idx]] = True
            tmp += 1
    if select[c] == False:
        tmp += 1
    answer = max(answer,tmp)

print(answer)    
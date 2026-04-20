import sys

input = sys.stdin.readline

n,m = map(int,input().split())

c1,c2 = map(int,input().split())

P = sorted(list(map(int,input().split())))

Q = sorted(list(map(int,input().split())))

answer_1 = int(1e9)
answer_2 = 0

for p in P:
    left, right = 0, m-1
    target = 0
    while left <= right:
        mid = (left+right)//2
        if Q[mid] <= p:
            target = mid
            left = mid + 1
        else:
            right = mid - 1
    if abs(p-Q[target]) < answer_1:
        answer_1 = abs(p-Q[target])
        answer_2 = 0
    if abs(p-Q[target]) == answer_1:
        answer_2 += 1
    if target == m-1: continue
    target+=1
    if abs(p-Q[target]) < answer_1:
        answer_1 = abs(p-Q[target])
        answer_2 = 0
    if abs(p-Q[target]) == answer_1:
        answer_2 += 1

answer_1 += abs(c1-c2)

print(answer_1,answer_2)
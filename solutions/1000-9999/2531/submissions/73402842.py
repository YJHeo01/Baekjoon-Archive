import sys

input = sys.stdin.readline

n,d,k,c = map(int,input().split())

belt = []

answer = 0
tmp = 0

for _ in range(n):
    belt.append(int(input()))

select = [0] * (d+1)

for i in range(k):
    if select[belt[i]] == 0:
        tmp += 1
    select[belt[i]] += 1

if select[c] == 0:
    answer = max(answer,tmp+1)
else:
    answer = max(answer,tmp)


for left in range(0,n):
    right = (left+k) % n
    select[belt[left]] -= 1
    if select[belt[left]] == 0:
        tmp -= 1
    if select[belt[right]] == 0:
        tmp += 1
    select[belt[right]] += 1
    if select[c] == 0:
        answer = max(answer,tmp+1)
    else:
        answer = max(answer,tmp)

print(answer)    
import sys

input = sys.stdin.readline

n,h = map(int,input().split())

high_block = [0] * (h+1)
low_block = [0] * (h+1)
for i in range(n):
    size = int(input())
    if i % 2 == 0:
        low_block[size] += 1
    else:
        high_block[h-size+1] += 1

for i in range(1,h+1):
    high_block[i] += high_block[i-1]

for i in range(h-1,-1,-1):
    low_block[i] += low_block[i+1]

INF = int(1e9)

sum_block = [0] * (h+1)

for i in range(h+1):
    sum_block[i] = high_block[i] + low_block[i]
sum_block = sum_block[1:h+1]
sum_block.sort()

first_answer = sum_block[0]

second_answer = 0

for i in sum_block:
    if first_answer == i:
        second_answer += 1
    else:
        break

print(first_answer,second_answer)
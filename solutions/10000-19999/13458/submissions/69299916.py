import sys
import math
input = sys.stdin.readline

n = int(input())

A_i = list(map(int,input().split()))

b,c = map(int,input().split())
answer = 0
for i in A_i:
    tmp = i - b
    answer += 1
    if tmp > 0:
        answer += math.ceil(tmp/c)
print(answer)
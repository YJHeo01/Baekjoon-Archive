import sys

input = sys.stdin.readline

n,k = map(int,input().split())
checkpoint = []

answer = 0

for _ in range(n):
    checkpoint.append(int(input()))

checkpoint.sort()

for i in range(n-1,-1,-k):
    answer += checkpoint[i]

answer *= 2

print(answer)
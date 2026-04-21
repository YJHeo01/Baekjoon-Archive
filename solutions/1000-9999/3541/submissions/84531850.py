import sys

input = sys.stdin.readline

n,m = map(int,input().split())

answer = int(1e9)

for _ in range(m):
    tmp = 0
    u,d = map(int,input().split())
    for _ in range(n):
        if tmp >= d:
            tmp -= d
        else:
            tmp += u
    answer = min(answer,tmp)

print(answer)
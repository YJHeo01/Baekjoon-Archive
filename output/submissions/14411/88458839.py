import sys

input = sys.stdin.readline

n = int(input())

pos = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:-x[0])

last_y = 0

answer = 0

for x,y in pos:
    if last_y > y: continue
    answer += (y-last_y) * x
    last_y = y

print(answer)
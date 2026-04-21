import sys

input = sys.stdin.readline

n = int(input())

flowers = []

for _ in range(n):
    flowers.append(list(map(int,input().split())))

start = 0
last_day = [3,1]
answer = 0

while last_day < [11,30]:
    next_last_day = last_day
    for i in range(n):
        if last_day < flowers[i][0:2]:
            continue
        if next_last_day < flowers[i][2:]:
            next_last_day = max(flowers[i][2:],next_last_day)
    answer += 1
    if last_day == next_last_day:
        answer = 0
        break
    last_day = next_last_day
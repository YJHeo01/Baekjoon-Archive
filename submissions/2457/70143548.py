import sys

input = sys.stdin.readline

n = int(input())

flowers = []

for _ in range(n):
    flowers.append(list(map(int,input().split())))

flowers.sort()
start = 0
last_day = [3,1]
answer = 0

for i in range(n):
    if last_day < flowers[i][0:2]:
        next_last_day = last_day
        answer += 1
        for j in range(i):
            if next_last_day < flowers[j][2:]:
                if flowers[j][0:2] > next_last_day:
                    continue
                next_last_day = flowers[j][2:]
        last_day = next_last_day

while last_day < [11,30]:
    for i in range(n):
        if next_last_day < flowers[i][2:]:
            if next_last_day < flowers[j][2:]:
                continue
            next_last_day = flowers[i][2:]
    answer += 1
    if last_day == next_last_day:
        answer = 0
        break
    last_day = next_last_day





print(answer)
    
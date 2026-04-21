import sys

input = sys.stdin.readline

visited_high = [False] * (500001)

n = int(input())

answer = 0

sky_line = []

for _ in range(n):
    sky_line.append(list(map(int,input().split())))

sky_line.sort()

for x,y in sky_line:
    if y == 0:
        visited_high = [False] * 500001
    elif visited_high[y] == False:
        visited_high[y] = True
        answer += 1
    else:
        continue

print(answer)
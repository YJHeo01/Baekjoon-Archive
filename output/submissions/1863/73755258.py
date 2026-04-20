import sys

input = sys.stdin.readline

visited_high = [False] * (500001)

n = int(input())

answer = 0

for _ in range(n):
    a,b = map(int,input().split())
    if b == 0:
        visited_high = [False] * (500001)
    elif visited_high[b] == False:
        visited_high[b] = True
        answer += 1
    else:
        continue

print(answer)
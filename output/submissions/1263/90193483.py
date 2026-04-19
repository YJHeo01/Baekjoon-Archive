import sys

input = sys.stdin.readline

n = int(input())

array = [list(map(int,input().split())) for _ in range(n)]

array.sort(key=lambda x:(-x[1],-x[0]))

answer = int(1e9)

for t,s in array:
    if answer > s: answer = s
    answer -= t

if answer < 0: answer = -1

print(answer)
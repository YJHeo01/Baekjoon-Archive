import sys

input = sys.stdin.readline

n = int(input())

water = list(map(int,input().split()))

q = int(input())

open = [1] * n

answer = sum(water)

print(answer)

for _ in range(q):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        answer -= water[tmp[1]-1]
        answer += tmp[2]
    else:
        open[tmp[1]-1] *= -1
        answer += (water[tmp[1]-1] * open[tmp[1]-1])
    print(answer)
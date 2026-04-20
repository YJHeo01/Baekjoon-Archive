import sys

input = sys.stdin.readline

n = int(input())

water = list(map(int,input().split()))

q = int(input())

open = [1] * n

print(sum(water))
for _ in range(q):
    answer = 0
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        water[tmp[1]-1] = tmp[2]
    else:
        open[tmp[1]-1] *= -1
    for i in range(n):
        if open[i] > 0:
            answer += water[i]
    print(answer)

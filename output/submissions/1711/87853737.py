from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())

dot = [list(map(int,input().split())) for _ in range(n)]

answer = 0

cases = list(combinations(range(3),2))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            dots = [dot[i],dot[j],dot[k]]
            lines = []
            for a,b in cases:
                x1,y1 = dots[a]
                x2,y2 = dots[b]
                lines.append((x1-x2)**2 + (y1-y2) ** 2)
            lines.sort()
            if sum(lines[:2]) ** 2 == lines[2] ** 2: answer += 1

print(answer)
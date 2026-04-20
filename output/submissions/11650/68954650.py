import sys

input = sys.stdin.readline

N = int(input())

xy = []
for i in range(N):
    x, y = map(int,input().split())
    xy.append((x,y))

xy.sort()

for i in range(N):
    print(xy[i][0], xy[i][1])
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

name = []
for _ in range(n):
    power, num = input().split()
    name.append((power,int(num)))

for _ in range(m):
    tmp = int(input())
    for i in name:
        if i[1] >= tmp:
            print(i[0])
            break
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

title_list = []

for _ in range(n):
    name, power = input().split()
    title_list.append((int(power),name))

title_list.sort()

for _ in range(m):
    power = int(input())
    for title in title_list:
        if power <= title[0]:
            print(title[1])
            break
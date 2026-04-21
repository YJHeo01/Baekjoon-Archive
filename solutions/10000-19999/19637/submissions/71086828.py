import sys

input = sys.stdin.readline

n,m = map(int,input().split())

title_list = []
powers = []
for _ in range(n):
    name, power = input().split()
    if power not in powers:
        title_list.append((int(power),name))
        powers.append(power)

title_list.sort()
l = len(powers)
for _ in range(m):
    power = int(input())
    left,right = 0,l
    print_idx = 0
    while left <= right:
        mid = (left + right) // 2
        if title_list[mid][0] < power:
            left = mid + 1
        else:
            right = mid - 1
            print_idx = mid
    print(title_list[print_idx][1])

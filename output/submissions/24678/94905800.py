import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sum_value = sum(map(int,input().split()))
    if sum_value % 3 == 0:
        print('B')
    else:
        print('R')
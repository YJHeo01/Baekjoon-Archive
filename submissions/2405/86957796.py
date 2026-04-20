import sys

input = sys.stdin.readline

n = int(input())

array = sorted([int(input()) for _ in range(n)])

print(max(abs((array[0]+array[1]+array[n-1])-array[1]*3),abs((array[0]+array[n-2]+array[n-1])-array[n-2]*3)))
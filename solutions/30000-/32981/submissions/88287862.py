import sys;sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(5)
    else:
        print(4*max(1,5*(n-1)))
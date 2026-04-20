import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
big = max(data)
small = min(data)

print(small,big)
import sys

input = sys.stdin.readline

n = int(input())

k = int(input())

for _ in range(k):
    x,y = map(int,input().split())
    tmp = min(x,n-x+1,y,n-y+1) % 3
    if tmp == 0: tmp = 3
    print(tmp)
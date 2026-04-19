import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p,q,r = map(int,input().split())
    answer = min(q,r) + min(p,r) - 1
    print(answer)
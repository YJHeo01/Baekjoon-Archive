import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    a %= 10
    answer = (a ** b) % 10
    print(answer)

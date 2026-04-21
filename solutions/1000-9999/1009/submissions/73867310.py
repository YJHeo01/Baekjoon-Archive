import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    a %= 10
    if a == 0:
        print("10")
        continue
    if b % 4 != 0:
        b %= 4
    else:
        b = 4
    answer = (a ** b) % 10
    if answer == 0:
        answer = 10
    print(answer)
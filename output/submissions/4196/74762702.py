import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    start = [True] * (n+1)
    answer = n
    for _ in range(m):
        a,b = map(int,input().split())
        if start[b] == True:
            start[b] = False
            answer -= 1
    if answer <= 0:
        answer = 1
    print(answer)

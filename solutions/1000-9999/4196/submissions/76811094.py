import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    start = [True] * (n+1)
    for _ in range(m):
        x,y = map(int,input().split())
        start[y] = False
    answer = 0
    for i in range(1,n+1):
        if start[i] == True:
            answer += 1
    print(answer)
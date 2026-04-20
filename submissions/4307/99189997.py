import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    min_answer,max_answer = 0,0
    l,n = map(int,input().split())
    for _ in range(n):
        x = int(input())
        min_answer = max(min_answer,min(x,l-x))
        max_answer = max(max_answer,l-x)
    print(min_answer,max_answer)
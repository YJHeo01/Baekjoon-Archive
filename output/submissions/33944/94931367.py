import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    x = int(input())
    p = list(map(int,input().split()))
    answer = 'POSSIBLE'
    if p[0] == 1:
        for i in range(x):
            if p[i] == 4:
                answer = 'IMPOSSIBLE'
    for i in range(3,x):
        tmp = True
        for j in range(3):
            if p[i-j-1] + 1 != p[i-j]: tmp = False
        if tmp:
            answer = 'IMPOSSIBLE'
            
    print(answer)
        
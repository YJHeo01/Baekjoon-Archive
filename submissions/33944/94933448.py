import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    x = int(input())
    p = list(map(int,input().split()))
    ham = set(p)
    pos = [False] * (x+1)
    pos[0] = True
    for i in range(x):
        if pos[i] == False: continue
        tmp = p[i]
        for dx in range(1,4):
            last_x = tmp - dx
            if last_x < 0: continue
            nx = last_x + 4
            if last_x in ham or nx in ham: continue
            for j in range(i,x):
                if nx < p[j]: 
                    pos[j+1] = True
                    break
                pos[j+1] = True
    if pos[x-1]: print("POSSIBLE")
    else: print("IMPOSSIBLE")
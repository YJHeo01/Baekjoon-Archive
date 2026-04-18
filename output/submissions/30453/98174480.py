import sys

input = sys.stdin.readline

n = int(input())

stars = []

for _ in range(n):
    stars.append(list(map(int,input().split())))
    
c = dict()

for i in range(n):
    for j in range(i,n):
        x = stars[i][0] + stars[j][0]
        y = stars[i][1] + stars[j][1]
        if (x,y) in c:
            c[(x,y)].add(i)
            c[(x,y)].add(j)
        else:
            c[(x,y)] = set([i,j])
            
answer = 0

for pos in c:
    answer = max(answer,len(c[pos]))

print(answer)
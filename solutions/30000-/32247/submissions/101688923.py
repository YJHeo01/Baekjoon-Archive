import sys

input = sys.stdin.readline

n,m = map(int,input().split())

a_x,a_y = 0,0
b_x,b_y = 0,0

query = [list(map(int,input().split())) for _ in range(m)]
query.append([1,n,1])
answer = "stay"

for c,x,h in query:
    if c == 0:
        a_x,a_y = x, h + 1
    else:
        h -= 1
        if (x-a_x) < (a_y-h):
            answer = "adios"

print(answer)
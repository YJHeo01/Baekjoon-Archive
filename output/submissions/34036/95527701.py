n = int(input())

d = dict()

answer = int(1e18)

for _ in range(n):
    x,s = map(int,input().split())
    for _ in range(1000000):
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
        x += s

for i in d:
    if d[i] == n:
        answer = min(answer,i)
    
if answer == int(1e18): answer = -1

print(answer)
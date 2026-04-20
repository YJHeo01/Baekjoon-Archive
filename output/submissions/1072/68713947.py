INF = int(1e10)
x, y = map(int,input().split())
z = (y*100)//x
min_v = 1
max_v = INF
answer = INF
while(min_v<=max_v):
    mid = (min_v+max_v)//2
    if z != (((y+mid)*100) // (x+mid)):
        answer = min(answer,mid)
        max_v = mid - 1
    else:
        min_v = mid + 1

if answer == INF:
    answer = -1
print(answer)
n,k = map(int,input().split())

gongU = list(map(int,input().split()))
team = list(map(int,input().split()))

restrict = [False] * n
cnt = 0

combo = []

for i in range(n):
    for j in range(n):
        combo.append((-gongU[i]*team[j],j))

combo.sort()

for score,idx in combo:
    if restrict[idx]: continue
    if cnt == k:
        print(-score)
        break
    restrict[idx] = True
    cnt += 1
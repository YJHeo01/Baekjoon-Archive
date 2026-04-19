INF = 1000

m = int(input())

k = int(input())

stone = list(map(int,input().split()))

lose = [False] * INF

for i in range(1,INF):
    for j in stone:
        if j > i: continue
        if lose[i-j] == False: lose[i] = True

cnt = 0

for i in range(1,INF):
    if lose[i] == False: cnt += 1

answer = cnt * (m//(INF-1))

tmp = m % (INF-1)

for i in range(1,tmp+1):
    if lose[i] == False: answer += 1
    
print(answer)
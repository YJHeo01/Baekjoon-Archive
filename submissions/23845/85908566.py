n = int(input())
INF = 100000
cnt = [0] * (INF+1)
array = list(map(int,input().split()))
for i in array: cnt[i] += 1
answer = 0
for i in range(INF,0,-1):
    tmp = cnt[i]
    for j in range(i,0,-1):
        tmp = min(cnt[j],tmp)
        if tmp == 0: break
        answer += tmp * i
        cnt[j] -= tmp
print(answer)
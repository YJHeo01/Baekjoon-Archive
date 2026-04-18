n,K = map(int,input().split())

stats = [list(map(int,input().split())) for _ in range(n)]

answer = int(1e9)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if stats[i][0] + stats[j][1] + stats[k][2] >= answer: continue
            cnt = 0
            for x in range(n):
                if stats[i][0] < stats[x][0]:
                    continue
                if stats[j][1] < stats[x][1]:
                    continue
                if stats[k][2] < stats[x][2]:
                    continue
                cnt += 1
            if cnt >= K:
                answer = stats[i][0] + stats[j][1] + stats[k][2]
                
print(answer)
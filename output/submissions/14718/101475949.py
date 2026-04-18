n,K = map(int,input().split())

stats = [list(map(int,input().split())) for _ in range(n)]

answer = int(1e9)

for i in range(n):
    for j in range(n):
        for k in range(n):
            arr = [stats[i][0], stats[j][1], stats[k][2]]
            if stats[i][0] + stats[j][1] + stats[k][2] >= answer: continue
            cnt = n
            for x in range(n):
                for y in range(3):
                    if stats[x][y] > arr[y]:
                        cnt -= 1
                        break
            if cnt >= K:
                answer = stats[i][0] + stats[j][1] + stats[k][2]
                
print(answer)
INF = 1000001

cnt = [0] * INF

for start in range(1,INF):
    idx = start
    for j in range(1,INF):
        idx += j
        if idx >= INF: break
        cnt[idx] += 1

while True:
    i = int(input())
    if i == 0: break
    print(cnt[i])
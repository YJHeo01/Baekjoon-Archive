n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
array.sort(key=lambda x:-x[2])
cnt = [0] * n
idx = -1
for _ in range(3):
    while True:
        idx += 1
        if cnt[array[idx][0]] >= 2: continue
        cnt[array[idx][0]] += 1
        print(*array[idx][:2])
        break
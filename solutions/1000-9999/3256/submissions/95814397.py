n = int(input())

r = [int(input()) for _ in range(n)]

cnt = [0] * 1001

l = 0

for i in range(n):
    if l > r[i]: continue
    l = r[i]
    cnt[r[i]] += 1

max_time = 0

answer = 0

last_visit = 1

for i in range(1,1001):
    if cnt[i] == 0: continue
    tmp = max_time + cnt[i] * 5 + (i-last_visit)
    answer = max(answer,tmp)
    max_time = max(max_time,answer)
    last_visit = i

print(answer)
import sys

input = sys.stdin.readline

n,t = map(int,input().split())

cnt = [0] * t

driver = [[] for _ in range(t)]

time = 0

for _ in range(n):
    di,ti = input().rstrip().split()
    ti = int(ti)
    time += ti
    time %= t
    cnt[time] += 1
    driver[time].append(di)

prefix_sum = [0] * (t+1)

for i in range(t):
    prefix_sum[i+1] = prefix_sum[i] + cnt[i]

for i in range(t):
    if i >= 1000:
        if prefix_sum[i] - prefix_sum[i-1000] >= 1:
            cnt[i] = -1 
    else:
        if prefix_sum[i] - prefix_sum[0] >= 1:
            cnt[i] = -1
        if prefix_sum[t] - prefix_sum[t-1000+i]:
            cnt[i] = -1

answer = []

for i in range(t):
    if cnt[i] == -1:
        answer += driver[i]
        
answer.sort()

if answer == []:
    print(-1)
else:
    print(*answer)

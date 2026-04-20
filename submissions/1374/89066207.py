import sys, heapq

input = sys.stdin.readline

n = int(input())

study = []

answer = 0

for _ in range(n):
    a,b,c = map(int,input().split())
    study.append((b,c))

study.sort()

cnt = 0

q = []

for start,end in study:
    while q:
        tmp = heapq.heappop(q)
        if tmp > start:
            heapq.heappush(q,tmp)
            break
        cnt -= 1
    cnt += 1
    heapq.heappush(q,end)
    answer = max(answer,cnt)

print(answer)
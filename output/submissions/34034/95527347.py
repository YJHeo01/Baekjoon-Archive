import heapq

n,m,k = map(int,input().split())

answer = [0] * k

q = []

problem = list(map(int,input().split()))

for i in range(n):
    heapq.heappush(q,(problem[i],i+1))

idx = 0

while q:
    need, p_num = heapq.heappop(q)
    if need + idx >= k:
        break
    idx += (need-1)
    answer[idx] = p_num
    idx += 1

st_cnt = 0

for i in answer:
    if i == 0: st_cnt += 1

if st_cnt > m:
    print(-1)
else:
    print(*answer)
from collections import deque

n,k = map(int,input().split())

arr = list(map(int,input().split()))

one_q = deque([])
two_q = deque([])

for i in range(n):
    if arr[i] == 1: one_q.append(i)
    else: two_q.append(i)
    
one_idx = 0
two_idx = 0

idx = 0

answer = 0

one_cnt = len(one_q)
two_cnt = len(two_q)

while one_idx < one_cnt and two_idx < two_cnt:
    tmp = 0
    if one_q[one_idx] < idx + k:
        tmp += 1
        one_idx += 1
    if two_q[two_idx] < idx + k:
        tmp += 1
        two_idx += 1
    idx += tmp
    answer += 1

answer += (one_cnt-one_idx)
answer += (two_cnt-two_idx)

print(answer)
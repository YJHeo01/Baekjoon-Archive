from collections import deque

n,k = map(int,input().split())

array = list(map(int,input().split()))

value_idx = [deque([]) for _ in range(100001)]

value_cnt = [0] * (100001)

left = 0
right = 0
answer = 0

while True:
    if right >= n:
        break
    value_idx[array[right]].append(right)
    if value_cnt[array[right]] == k:
        answer = max(answer,right - left)
        value_first_idx = value_idx[array[right]].popleft()
        for i in range(left,value_first_idx):
            value_cnt[array[i]] -= 1
        left = value_first_idx + 1
        right += 1
    else:
        value_cnt[array[right]] += 1
        right += 1
        answer = max(answer,right-left)

print(answer)
n,k = map(int,input().split())

array = list(map(int,input().split()))

value_first_idx = [-1] * (100001)

value_cnt = [0] * (100001)

left = 0
right = 0
answer = 0

while True:
    if right >= n:
        break
    if value_cnt[array[right]] == 0:
        value_first_idx[array[right]] = right
        value_cnt[array[right]] = 1
        right += 1
        answer = max(answer,right-left)
    elif value_cnt[array[right]] == k:
        answer = max(answer,right - left)
        left = value_first_idx[array[right]] + 1
        right = left
        value_cnt = [0] * (100001)
    else:
        value_cnt[array[right]] += 1
        right += 1
        answer = max(answer,right-left)

print(answer)
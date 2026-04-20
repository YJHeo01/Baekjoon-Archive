n = list(input())

set_cnt = [0] * 10

for i in n:
    set_cnt[int(i)] += 1

set_cnt[9] += set_cnt[6]
set_cnt[9] = set_cnt[9] // 2 + set_cnt[9] % 2
set_cnt[6] = 0

answer = max(set_cnt)

print(answer)
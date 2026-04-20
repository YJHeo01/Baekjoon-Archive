from collections import deque

n,k = map(int,input().split())

line_up = list(map(int,input().split()))

next_use_order = [deque([]) for _ in range(k+1)]

multi_tap = []

for i in range(k):
    next_use_order[line_up[i]].append(i)

answer = 0
start = k

for i in range(k):
    idx = line_up[i]
    next_use_order[idx].popleft()
    if idx in multi_tap:
        continue
    multi_tap.append(idx)
    if len(multi_tap) == n:
        start = i + 1
        break

for i in range(start,k):
    idx = line_up[i]
    next_use_order[idx].popleft()
    if idx in multi_tap:
        continue
    answer += 1
    remove_idx = -1
    remove_idx_next_order = 0
    for j in multi_tap:
        if next_use_order[j] == deque([]):
            remove_idx = j
            break
        if remove_idx_next_order < next_use_order[j][0]:
            remove_idx_next_order = next_use_order[j][0]
            remove_idx = j
    multi_tap.remove(remove_idx)
    multi_tap.append(idx)

print(answer)
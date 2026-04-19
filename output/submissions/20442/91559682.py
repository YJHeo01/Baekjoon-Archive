s = list(input())

length = len(s)

r_cnt = 0

for c in s:
    if c == 'R': r_cnt += 1

answer = r_cnt

k_cnt = 0

left, right = -1, length

while True:
    while left < length:
        left += 1
        if left == length: break
        if s[left] == 'K':
            k_cnt += 1
            break
        r_cnt -= 1
    while right >= 0:
        right -= 1
        if right < 0: break
        if s[right] == 'K':
            k_cnt += 1
            break
        r_cnt -= 1
    if left > right or r_cnt <= 0: break
    answer = max(answer,r_cnt+k_cnt)
    
print(answer)
s = "." + input()

l = len(s)

answer = (1,1,1)

left = 1

B_cnt = 0

for right in range(1,l):
    if s[right] == 'B': B_cnt += 1
    else: B_cnt -= 1
    if B_cnt > answer[0]:
        answer = (B_cnt,left,right)
    if B_cnt < 0:
        B_cnt = 0
        left = right + 1

R_cnt = 0

left = 1

for right in range(1,l):
    if s[right] == 'R': R_cnt += 1
    else: R_cnt -= 1
    if R_cnt > answer[0]:
        answer = (R_cnt,left,right)
    if R_cnt < 0:
        R_cnt = 0
        left = right + 1
        
print(*answer[1:])
left_vip = 0
n = int(input())
m = int(input())
answer = 1
for _ in range(m):
    right_vip = int(input())
    if right_vip -1 != left_vip:
        answer *= (right_vip-left_vip-1)
    left_vip = right_vip

right_vip = n

if left_vip != right_vip:
    answer *= (right_vip-left_vip)

print(answer)
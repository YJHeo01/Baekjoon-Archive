n = int(input())
m = int(input())

left = 0

answer = 1
for _ in range(m):
    right = int(input())
    if left + 1 == right:
        left = right
        continue
    answer *= (right - left - 1)
    left = right

if left != n-1:
    answer *= (n-left)

print(answer)
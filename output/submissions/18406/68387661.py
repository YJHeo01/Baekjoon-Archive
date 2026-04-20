n = input()

l = len(n)
sum_left = 0
sum_right = 0
for i in range(0,l//2):
    sum_left += int(n[i])
for j in range(l//2,l):
    sum_right += int(n[j])

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")
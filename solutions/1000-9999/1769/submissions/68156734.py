n = int(input())
three = 0
cnt = 0
sum = 0
while(1):
    if n < 10:
        if n % 3 == 0:
            three = 1
        break
    cnt += 1
    while(n>0):
        sum = sum + n % 10
        n = n // 10
    n = sum
    sum = 0

print(cnt)
if three == 0:
    print("NO")
else : print("YES")
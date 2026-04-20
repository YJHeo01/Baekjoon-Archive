n = int(input())
cnt = 1
tmp = 0
while 1:
    tmp = 0
    while n:
        tmp += (n % 10)
        n = n // 10
    if tmp < 10:
        break
    cnt += 1
    n = tmp

print(cnt)
if tmp % 3 ==0:
    print("YES")
else:
    print("NO")
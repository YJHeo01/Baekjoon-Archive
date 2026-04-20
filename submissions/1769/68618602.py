n = input()
cnt_zero = 0
if len(n) == 1:
    cnt_zero = 1
cnt = 1
while(1):
    tmp = 0
    n = list(n)
    for i in n:
        tmp += i
    if tmp < 10:
        break    
    cnt += 1
    n = str(tmp)

if cnt_zero == 1:
    print("0")
else:
    print(cnt)

if tmp % 3 == 0:
    print("YES")
else:
    print("NO")
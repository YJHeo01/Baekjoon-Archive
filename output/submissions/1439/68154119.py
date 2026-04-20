s = list(input())

cnt = 0

l = len(s)
if l == 1:
    print("0")
else:
    for i in range(1,l):
        if s[i] != s[i-1]:
            cnt += 1
    if cnt % 2 == 1: cnt += 1
    cnt = cnt // 2
    print(cnt)
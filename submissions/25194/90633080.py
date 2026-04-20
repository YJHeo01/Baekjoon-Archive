n = int(input())

week = [False] * 7
week[0] = True

arr = list(map(int,input().split()))

for i in arr:
    tmp = [False] * 7
    for j in range(7):
        if week[j]:
            tmp[(j+i)%7] = True
    for j in range(7):
        week[j] |= tmp[j]
        
if week[4]:
    print("YES")
else:
    print("NO")
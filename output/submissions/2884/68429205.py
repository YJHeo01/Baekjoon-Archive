h,m = map(int,input().split())

if m >= 45:
    m -= 45
elif h>0:
    m += 15
    h-=1
else:
    h = 23
    m+= 15

print(h,end = ' ')
print(m)
h,w,n,m = map(int,input().split())

x = h//(n+1)
if h % (n+1) != 0:
    x += 1

y = w // (m+1)
if w % (m+1) != 0:
    y += 1

answer = x * y

print(answer)
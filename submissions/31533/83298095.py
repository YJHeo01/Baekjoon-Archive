a = int(input())
m,n = map(int,input().split())
if a != 1:
    time = 2 * min(m,n)
else:
    time = min(min(m,n)*2,max(n,m))
print(time/a)
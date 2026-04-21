n = int(input())
a = list(map(int,input().split()))
a.sort()
if n % 2 == 0:
    i = int((1+n)/2)
    A = a[i] * a[i-1]
else:
    i = int(((1+n)/2))
    A = (a[i-1]) ** 2
print(A)
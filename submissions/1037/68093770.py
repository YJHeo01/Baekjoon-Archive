n = int(input())
a = list(map(int,input().split()))
a.sort()
if n % 2 == 0:
    A = a[0] * a[-1]
else:
    i = int(((n-1)/2))
    A = (a[i]) ** 2
print(A)
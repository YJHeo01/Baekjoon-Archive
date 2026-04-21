m,n = map(int,input().split())

if abs(m) == 1 or abs(n) == 1:
    print(1)
elif m % n == 0 or n % m == 0:
    print(2)
else:
    print(1)
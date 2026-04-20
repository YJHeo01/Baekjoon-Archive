t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    tmp = a ** b
    tmp %= 10
    if tmp == 0:
        tmp += 10
    print(tmp)
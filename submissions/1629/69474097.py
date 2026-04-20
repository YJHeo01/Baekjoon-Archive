def cal(a,b,c):
    if b == 0:
        return 0
    if b == 1:
        return a
    v1 = cal(a,b//2,c)
    if b % 2 == 1:
        b+=1
    v2 = cal(a,b//2,c)
    return v1*v2 % c

a,b,c = map(int,input().split())

answer = cal(a%c,b%c,c)

print(answer)
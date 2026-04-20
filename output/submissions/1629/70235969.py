a,b,c = map(int,input().split())

def cal(a,b,c):
    if b == 1:
        return a % c
    if b % 2 == 1:
        return (a * (cal(a,b//2,c) ** 2))%c
    else:
        return ((cal(a,(b//2),c)**2))%c
        
answer = cal(a,b,c)

print(answer)
def Euclidean(a,b):
    if b == 0:
        return a
    return Euclidean(b,a%b)

a,b = map(int,input().split())

if b > a:
    a,b = b,a

print(a*b//Euclidean(a,b))
def Euclidean(a,b):
    if b == 0:
        return a
    return Euclidean(b,a%b)

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(a*b//Euclidean(a,b))
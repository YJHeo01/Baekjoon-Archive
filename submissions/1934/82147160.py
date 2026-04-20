import sys

input = sys.stdin.readline

def Euclidean(a,b):
    if b == 0:
        return a
    return Euclidean(b,a%b)

for _ in range(int(input())):
    a,b = map(int,input().split())
    if b > a:
        a,b = b,a
    tmp = Euclidean(a,b)
    print(a*b//tmp)

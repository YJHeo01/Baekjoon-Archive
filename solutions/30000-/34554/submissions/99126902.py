import sys, math
 
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a,b = 1, n + 1
    for i in range(2,int(math.sqrt(n+1))+1):
        if b % i == 0:
            a = -1
    if a == -1:
        print(0)
    else:
        print(1)
        print(a,b)

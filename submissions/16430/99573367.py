a,b=map(int,input().split())
a = b-a
for i in range(1,10):
    if a % i == 0 and b %i == 0:
        a %= i
        b %= i
        
print(a,b)
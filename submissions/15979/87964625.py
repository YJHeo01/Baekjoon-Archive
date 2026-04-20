m,n = map(int,input().split())

m,n = abs(m), abs(n)
if n > m: m,n = n,m

def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)
    
gcdgcd = gcd(m,n)

if m == 0 and n == 0:
    print(0)
elif gcdgcd == 1:
    print(1)
else:
    print(2)
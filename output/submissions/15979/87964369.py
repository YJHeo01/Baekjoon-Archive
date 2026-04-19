m,n = map(int,input().split())

if n > m: n,m = m,n

def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)
    
gcdgcd = gcd(m,n)

if gcdgcd == 1:
    print(1)
else:
    print(2)
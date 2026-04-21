n,k = map(int,input().split())
array = list(map(int,input().split()))
answer = "YES"

def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)

for i in range(n):
    if array[i] % gcd(n,k) != i % gcd(n,k):
        answer = "NO"

print(answer)
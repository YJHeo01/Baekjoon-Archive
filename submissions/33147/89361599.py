n,k = map(int,input().split())
array = list(map(int,input().split()))
answer = "YES"

gcd = n

div = k

while True:
    if div == 0: break
    tmp = div
    div = gcd % div
    gcd = tmp

for i in range(n):
    if array[i] % gcd != i % gcd:
        answer = "NO"

print(answer)
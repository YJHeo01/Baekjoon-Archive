a,b,n,k = map(int,input().split())

answer = 0

while True:
    if k <= n: break
    answer += 1
    k -= n

i = (answer // b) + 1

j = answer % b + 1

print(i,j)
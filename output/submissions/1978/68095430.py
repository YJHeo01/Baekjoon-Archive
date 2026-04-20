n = int(input())

l = list(map(int,input().split()))

cnt = 0

for i in l:
    if n % i:
        cnt+=1

print(cnt)
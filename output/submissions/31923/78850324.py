n,p,q = map(int,input().split())

yes = True
answer = [0] * n
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(n):
    cnt = 0
    while True:
        if a[i] == b[i]:
            break
        if cnt > 10000:
            yes = False
            break
        cnt += 1
        a[i] += p
        b[i] += q
    answer[i] = cnt
        
if yes == True:
    print('YES')
    for i in answer:
        print(i,end=" ")
else:
    print('NO')
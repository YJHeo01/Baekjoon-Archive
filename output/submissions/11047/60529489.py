n,k = map(int,input().split())

array = []

for i in range(n):
    tmp = int(input())
    if tmp < k:
        array.append(tmp)
    else : break

cnt = 0
for i in range(len(array)-1,-1,-1):
    cnt += k // array[i]
    k = k % array[i]
    if k == 0 : break

print(cnt)
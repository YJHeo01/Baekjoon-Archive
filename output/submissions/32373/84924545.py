n,k = map(int,input().split())
A = list(map(int,input().split()))
a = 'Yes'
for i in range(n):
    if(A[i]-i)%k!=0:a='No'
print(a)
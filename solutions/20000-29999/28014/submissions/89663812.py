n = int(input())

A = list(map(int,input().split()))

a = 1

for i in range(1,n):
    if A[i] >= A[i-1]: a += 1
    
print(a)
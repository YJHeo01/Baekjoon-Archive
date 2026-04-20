n = int(input())
A = sorted([int(input())for _ in range(n)])
a = 0
for i in range(1,n-1):a = max(a,abs(A[i]*2-A[0]-A[i+1]),abs(A[i]*2-A[i-1]-A[n-1]))
print(a)
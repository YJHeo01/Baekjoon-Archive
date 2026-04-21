n = int(input())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

C = list(map(int,input().split()))

A_idx = [0] * (n+1)

B_idx = [0] * (n+1)

C_idx = [0] * (n+1)

answer = 0

for i in range(n):
    A_idx[A[i]] = i
    B_idx[B[i]] = i
    C_idx[C[i]] = i
    
for i in range(1,n+1):
    tmp = set(A[:A_idx[i]]) & set(B[:B_idx[i]]) & set(C[:C_idx[i]])
    if tmp == set(): answer += 1
    
print(answer)
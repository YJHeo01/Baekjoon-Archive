n = int(input())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

C = list(map(int,input().split()))

max_idx = [0] * (n+1)
min_idx = [0] * (n+1)

A_idx = [0] * (n+1)

B_idx = [0] * (n+1)

C_idx = [0] * (n+1)

answer = 0

for i in range(n):
    A_idx[A[i]] = i
    B_idx[B[i]] = i
    C_idx[C[i]] = i
    
for i in range(1,n+1):
    max_idx[i] = max(A_idx[i],B_idx[i],C_idx[i])
    min_idx[i] = min(A_idx[i],B_idx[i],C_idx[i])

target_idx = 1

for i in range(2,n+1):
    if max_idx[i] < max_idx[target_idx]:
        target_idx = i

answer = 0

for i in range(1,n+1):
    if min_idx[i] > max_idx[target_idx]: continue
    tmp = set(A[:A_idx[i]]) & set(B[:B_idx[i]]) & set(C[:C_idx[i]])
    if tmp == set(): answer += 1

print(answer)
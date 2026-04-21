n = int(input())

A = list(map(int,input().split()))

length = [1] * n

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            length[i] = max(length[j]+1,length[i])

print(max(length))
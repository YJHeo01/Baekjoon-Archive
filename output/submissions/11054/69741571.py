n = int(input())

A = list(map(int,input().split()))

length = [1] * n
length_ = [1] * n
for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            length[i] = max(length[j]+1,length[i])

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if A[i] > A[j]:
            length_[i] = max(length_[i],length_[j]+1)


answer = 0

for i in range(n):
    answer = max(answer,length[i]+length_[i])

print(answer-1)
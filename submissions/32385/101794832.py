n = int(input())

A_n_1 = n + 1

tmp = 0

for i in range(n-1):
    print(A_n_1-1-i,end=" ")
    
print(A_n_1+n*(n-1)//2,end=" ")

print(A_n_1)
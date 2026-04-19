n = int(input())
for i in range(n):
    if i % 2 == 0:
        print(n-i//2,end=" ")
    else:
        print(1+i//2,end=" ")
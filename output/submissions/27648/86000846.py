n,m,k = map(int,input().split())

if n + m > k:
    print("NO")
    exit(0)

print("YES")

for i in range(n):
    for j in range(m):
        print(i+j+1,end=" ")
    print()
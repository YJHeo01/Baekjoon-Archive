n,m,k = map(int,input().split())

if n + m > k:
    print("NO")
    exit(0)

print("YES")

for i in range(1,n+1):
    for j in range(m):
        print(i+j,end=" ")
    print()
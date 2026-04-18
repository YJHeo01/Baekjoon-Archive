n = int(input())

a = []

for _ in range(n):
    tmp = input().split()
    name = tmp[0]
    year = int(tmp[1])
    a.append((year,name))

a.sort()

print(a[n-1][1])
n = int(input())

pole = []

for _ in range(n):
    pole.append(list(map(int,input().split())))

pole.sort()
arr = []
for i in range(n):
    arr.append(pole[i][1])

length = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            length[i] = max(length[i],length[j]+1)

print(n-max(length))
n = int(input())

array = list(map(int,input().split()))
change = []

for i in range(n):
    target = i + 1
    if array[i] == target: continue
    for j in range(i+1,n):
        if array[j] == target:
            change.append((i+1,j+1))
            array[i], array[j] = array[j], array[i]
            break

print(len(change))

for s in change:
    print(*s)
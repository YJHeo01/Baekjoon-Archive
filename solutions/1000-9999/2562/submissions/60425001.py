biggest = 0
tmp = 0
for i in range(9):
    n = int(input())
    if biggest < n :
        tmp = i + 1
        biggest = n

print(biggest)
print(tmp)
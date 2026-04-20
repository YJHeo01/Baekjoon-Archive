n = int(input())
array = []
for i in range(n):
    array.append(list(input()))

for i in range(len(array[0])):
    for j in range(1,n):
        if array[0][i] != array[j][i] :
            array[0][i] = '?'
            break
    print(array[0][i], end = '')
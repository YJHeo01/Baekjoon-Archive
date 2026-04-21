def comp(array1,array2,array3):
    cnt = 0
    for i in range(4):
        if array1[i] != array2[i]:
            cnt += 1
        if array1[i] != array3[i]:
            cnt += 1
        if array2[i] != array3[i]:
            cnt += 1
    return cnt

t = int(input())

for i in range(t):
    n = int(input())
    array = list(input().split())
    distance = []
    for j in range(0,n-2):
        for k in range(j+1,n-1):
            for l in range(k+1,n):
                a = comp(array[j],array[k],array[l])
                distance.append(a)
    distance.sort()
    print(distance[0])
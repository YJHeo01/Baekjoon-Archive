n,k = map(int,input().split())

array = list(input())

for i in range(k):
    finish = True
    for j in range(1,n-i):
        if int(array[j]) > int(array[j-1]):
            array = array[:j-1] + array[j:]
            finish = False
            break
    if finish == True:
        break

for i in range(n-k):
    print(array[i],end="")
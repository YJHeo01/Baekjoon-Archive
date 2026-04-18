n,m = map(int,input().split())

num_list = []

num_list.append((0,1))
num_list.append((1,1))

def Euclidean(a,b):
    if b == 0: return a
    return Euclidean(b,a%b)

for i in range(2,n+1):
    for j in range(i):
        tmp = Euclidean(i,j)
        if tmp == 1:
            num_list.append((j,i))

num_list.sort(key=lambda x:x[0]/x[1])

m -= 1

print(*num_list[m])
def Euclidean(a,b):
    if b == 0: return a
    return Euclidean(b,a%b)

for _ in range(int(input())):
    array = list(map(int,input().split()))
    answer = 0
    for i in range(1,array[0]+1):
        for j in range(1,i):
            answer += Euclidean(array[i],array[j])
    print(answer)

INF = 100001
measure = [[] for _ in range(INF)]
for i in range(2,INF):
    for j in range(i,INF,i):
        measure[j].append(i)
while True:
    n = int(input())
    if n == -1: break
    print(n,end=" ")
    if sum(measure[n]) - n + 1 == n:
        print("= 1",end=" ")
        for i in measure[n]:
            if i == n:
                print()
                break
            print("+",end=" ")
            print(i,end=" ")
    else:
        print("is NOT perfect.")
n = int(input())

array = list(map(int,input().split()))

value = [0] * 1001

for i in array: value[i] += 1

for i in range(1001):
    if value[i] == 0: continue
    if i != 1000 and value[i+1] != 0:
        if value[i] + value[i+1] == n:
            for _ in range(value[i+1]):
                print(i+1,end=" ")
            n -= value[i+1]
            value[i+1] = 0
        else:
            for _ in range(value[i]):
                print(i,end=" ")
            for j in range(i+2,1001):
                if value[j] != 0:
                    print(j,end=" ")
                    value[j] -= 1
                    n -= 1
                    break
            n -= value[i]
            value[i] = 0
            continue
    for _ in range(value[i]):
        print(i,end=" ")
    n -= value[i]
    value[i] = 0
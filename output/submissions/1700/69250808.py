n, k = map(int,input().split())

name = list(map(int,input().split()))

l = k // n
answer = 0
for i in range(l):
    multi = name[i*n:(i+1)*n]
    new = name[(i+1)*n:min((i+2)*n,k)]
    for j in new:
        if j not in multi:
            answer += 1
            multi.append(j)

print(answer)
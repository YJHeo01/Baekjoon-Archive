p,m,c = map(int,input().split())
x = int(input())

answer = int(1e13)

for i in range(1,p+1):
    for j in range(1,m+1):
        for k in range(1,c+1):
            answer = min(answer,abs((i+j)*(j*k)-x))

print(answer)
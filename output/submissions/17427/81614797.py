n = int(input())

answer = 1

tmp = [1] * (n+1)

for i in range(2,n+1):
    for j in range(i,n+1,i):
        tmp[j] += i
    answer += tmp[i]

print(answer)
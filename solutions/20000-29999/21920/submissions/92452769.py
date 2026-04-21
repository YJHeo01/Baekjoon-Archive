n = int(input())

arr = list(map(int,input().split()))

x = int(input())

INF = 1000001

prime = [True] * INF

prime_list = []

for i in range(2,INF):
    if prime[i]:
        for j in range(i+i,INF,i):
            prime[j] = False
        if x % i == 0:
            prime_list.append(i)

prime_list.append(x)

cnt = 0

value = 0

for a in arr:
    tmp = True
    for i in prime_list:
        if a % i == 0: tmp = False
    if tmp:
        cnt += 1
        value += a

print(value/cnt)
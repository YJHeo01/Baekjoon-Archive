n = int(input())

INF = 5000001
prime = [True] * (INF)

prime_factors = [[] for _ in range(INF)]

for i in range(2,INF):
    if prime[i] == True:
        for j in range(i,INF,i):
            prime[j] = False
            prime_factors[j].append(i)
array = list(map(int,input().split()))

for i in range(n):
    target = array[i]
    for prime_factor in prime_factors[array[i]]:
        while True:
            if target % prime_factor != 0:
                break
            target = target // prime_factor
            print(prime_factor,end=" ")
    print()
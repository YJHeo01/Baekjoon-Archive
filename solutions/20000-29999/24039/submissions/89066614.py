INF = 10001

n = int(input())

prime = [True] * INF
    
prime_list = []

for i in range(2,INF):
    if prime[i]:
        prime_list.append(i)
        for j in range(i,INF,i):
            prime[j] = False
    
prime_cnt = len(prime_list)

for i in range(1,prime_cnt):
    if prime_list[i-1] * prime_list[i] > n:
        print(prime_list[i-1]*prime_list[i])
        break

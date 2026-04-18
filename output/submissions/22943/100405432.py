k,m = map(int,input().split())

prime = []

sieve = [True] * 100000

for i in range(2,100000):
    if sieve[i] == False: continue
    prime.append(i)
    for j in range(i,100000,i):
        sieve[j] = False

l = len(prime)

possible = [False] * 100000

for i in prime:
    for j in prime:
        tmp = i * j
        if tmp >= 100000: break
        possible[tmp] = True

max_limit = 10 ** k
min_limit = 10 ** (k-1) - 1

answer = 0

for i in range(1,l):
    for j in range(i):
        value = prime[i] + prime[j]
        if value >= max_limit: break
        if value <= min_limit: continue
        cnt = [0] * 10
        tmp = value
        while tmp:
            cnt[tmp%10] += 1
            tmp //= 10
        if max(cnt) >= 2: continue
        while True:
            if value % m != 0: break
            value //= m
        if possible[value]:answer += 1
        
print(answer)
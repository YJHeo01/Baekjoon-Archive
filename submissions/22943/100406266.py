k,m = map(int,input().split())

prime = []

sieve = [True] * 100000

for i in range(2,100000): #소수 목록 구함
    if sieve[i] == False: continue
    prime.append(i)
    for j in range(i,100000,i):
        sieve[j] = False

l = len(prime)

possible = [False] * 100000 #True시 2번 조건 충족

for i in prime:
    for j in prime:
        tmp = i * j
        if tmp >= 100000: break
        possible[tmp] = True #2번 조건

max_limit = 10 ** k #10의 k승 == k+1가지 번호 사용
min_limit = 10 ** (k-1) - 1

#print(max_limit,min_limit)
answer = 0

for i in range(l):
    for j in range(i+1,l):
        value = prime[i] + prime[j]#1번 조건
        if value >= max_limit: break #숫자 개수
        if value <= min_limit: continue #숫자 개수
        cnt = [0] * 10
        tmp = value
        while tmp: #숫자를 한 번씩만 사용했는지 판별
            cnt[tmp%10] += 1
            tmp //= 10
        if max(cnt) >= 2: continue
        while True: #M으로 나누어 떨어질 때까지 나눔
            if value % m != 0: break
            value //= m
        if possible[value]: answer += 1 #2본 조건 충족시
print(answer)
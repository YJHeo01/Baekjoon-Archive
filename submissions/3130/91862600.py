from itertools import product

n,m = map(int,input().split())

pelin = []

for test_case in list(product(range(10),repeat=n//4+(n//2)%2)):
    tmp = ""
    for i in range(n//2):
        tmp += str(test_case[min(i,n//2-i-1)])
    pelin.append(tmp)

l = 10 ** (n//4 + (n//2)%2)

mod_front = [0] * m
mod_end = [0] * m

for i in range(l):
    mod_end[int(pelin[i])%m] += 1
    if pelin[i][0] != '0':
        mod_front[(int(pelin[i])*10**(n//2))%m] += 1

answer = mod_front[0] * mod_end[0]

for i in range(1,m):
    answer += mod_front[i] * mod_end[m-i]

print(answer)
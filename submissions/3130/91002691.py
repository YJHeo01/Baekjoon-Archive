from itertools import product

n,m = map(int,input().split())

pelin = []

for test_case in list(product(range(10),repeat=n//4+(n//2)%2)):
    tmp = ""
    for i in range(n//2):
        tmp += str(test_case[min(i,n//2-i-1)])
    pelin.append(tmp)

l = 10 ** (n//4 + (n//2)%2)

answer = 0

for i in range(l):
    if pelin[i][0] == '0': continue
    for j in range(l):
        tmp = int(pelin[i]+pelin[j])
        if tmp % m == 0: answer += 1
        
print(answer)
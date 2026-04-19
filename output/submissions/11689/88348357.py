from itertools import combinations

n = int(input())

answer = n

div_num = []

INF = int(1e6)

prime = [True] * INF
for i in range(2,INF):
    if prime[i] == True:
        if n % i == 0 and i != n: div_num.append(i)
        for j in range(i+i,INF,i):
            prime[j] = False

div_num_cnt = len(div_num)

for cnt in range(1,div_num_cnt+1):
    for test_case in list(combinations(div_num,cnt)):
        tmp = 1
        for tmptmp in test_case:
            tmp *= tmptmp
        if cnt % 2 == 1:
            answer -= (n//tmp)
        else:
            answer += (n//tmp)
if n != 1 and answer == n: answer -= 1
print(answer)
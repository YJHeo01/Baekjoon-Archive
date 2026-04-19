from itertools import combinations

prime = [True] * 10000

prime[0], prime[1] = False, False

for i in range(2,10000):
    if prime[i]:
        for j in range(i+i,10000,i):
            prime[j] = False

n,m = map(int,input().split())

arr = list(map(int,input().split()))

data = range(n)

test_case_list = list(combinations(data,m))

answer = []

for test_case in test_case_list:
    tmp = 0
    for i in test_case:
        tmp += arr[i]
    if prime[tmp] == True:
        prime[tmp] = False
        answer.append(tmp)

answer.sort()

if answer == []:
    print(-1)
else:
    print(*answer)
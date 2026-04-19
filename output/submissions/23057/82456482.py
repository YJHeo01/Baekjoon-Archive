from itertools import combinations

n = int(input())

data = list(range(n))

setset = set({})

card = list(map(int,input().split()))

for i in range(1,n+1):
    for test_case in list(combinations(data,i)):
        tmp = 0
        for idx in test_case:
            tmp += card[idx]
        if tmp not in setset:
            setset.add(tmp)

answer = sum(card) - len(setset)

print(answer)
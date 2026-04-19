from itertools import permutations

S = list(input())

length = len(S)

data = list(range(length))

exist = set()

answer = 0

for test_case in list(permutations(data,length)):
    tmp = ""
    for i in test_case:
        tmp += S[i]
    if tmp in exist: continue
    check = True
    for i in range(1,length):
        if tmp[i] == tmp[i-1]:
            check = False
            break
    if check:
        answer += 1
        exist.add(tmp)
        
print(answer)
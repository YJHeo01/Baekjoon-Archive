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
    exist.add(tmp)
    answer += 1 
    for i in range(1,length):
        if tmp[i] == tmp[i-1]:
            answer -= 1
            break
print(answer)
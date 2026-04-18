from itertools import permutations

n = int(input())

number = []

alphabet = dict()

for _ in range(n):
    s = input()
    for c in s:
        if c not in alphabet:
            alphabet[c] = len(alphabet)
    number.append(s)

data = list(range(len(alphabet)))

answer = 0

for test_case in list(permutations(data,len(data))):
    value = 0
    for s in number:
        tmp = 0
        for c in s:
            tmp *= 10
            tmp += (9 - test_case[alphabet[c]])
        value += tmp
    answer = max(answer,value)
    
print(answer)
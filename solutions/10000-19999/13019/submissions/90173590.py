A = list(input())
B = list(input())

alphabet_A = dict()
alphabet_B = dict()

for c in A:
    if c not in alphabet_A:
        alphabet_A[c] = 1
    else:
        alphabet_A[c] += 1

for c in B:
    if c not in alphabet_B:
        alphabet_B[c] = 1
    else:
        alphabet_B[c] += 1

for c in A:
    if c not in B or alphabet_A[c] != alphabet_B[c]:
        print(-1)
        exit(0)

answer = 0

while B:
    target = B.pop()
    while A:
        tmp = A.pop()
        if tmp == target: break
        answer += 1

print(answer)
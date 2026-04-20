T = input()
P = input()

n = len(T)
m = len(P)

pi = [0] * m

j = 0

for i in range(1,m):
    while j and P[i] != P[j]:
        j = pi[j-1]
    if P[i] == P[j]:
        j += 1
        pi[i] = j
        
j = 0

answer = []

for i in range(n):
    while j and T[i] != P[j]:
        j = pi[j-1]
    if T[i] == P[j]:
        if j == m-1:
            answer.append(i-m+2)
            j = pi[j]
        else:
            j += 1

print(len(answer))      

for pos in answer:
    print(pos)
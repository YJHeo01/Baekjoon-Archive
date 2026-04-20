#https://github.com/YJHeo01

L,R = input().split()

L = list(L)
R = list(R)


answer = 0

if len(L) == len(R):
    while answer < len(L):
        if L[answer] == '8' and R[answer] == '8':
            answer += 1
        else:
            break

print(answer)
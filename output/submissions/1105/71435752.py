#https://github.com/YJHeo01

L,R = input().split()

L = list(L)
R = list(R)


answer = 0
tmp = 0
if len(L) == len(R):
    while tmp < len(L):
        if L[tmp] == R[tmp]:
            if L[tmp] == '8':
                answer += 1
            tmp += 1
        else:
            break

print(answer)

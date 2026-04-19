prime = [True] * 301

prime[0], prime[1] = False, False

for i in range(2,301):
    if prime[i]:
        for j in range(i+i,301,i):
            prime[j] = False

for _ in range(int(input())):
    n = int(input())
    answer = [0] * n
    idx = 0
    for i in range(n+1):
        if prime[i]:
            answer[idx] = i
            idx += 2
    idx = 0
    for i in range(1,n+1):
        if prime[i]: continue
        while True:
            if answer[idx] == 0: break
            idx += 1
        answer[idx] = i
    print("YES")
    print(*answer)
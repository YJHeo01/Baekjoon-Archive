N, M = map(int,input().split())

price_p = [ [0] for _ in range(M) ]
price_s = [ [0] for _ in range(M) ]
for i in range(M):
    price_p[i], price_s[i] = map(int,input().split())

p_min = min(price_p)
s_min = min(price_s)

if p_min >= 6*s_min:
    print(N*s_min)
else :
    answer = (N // 6) * p_min
    mod = N % 6
    if p_min > s_min * mod:
        answer += s_min * mod
    else : answer += p_min
    print(answer)
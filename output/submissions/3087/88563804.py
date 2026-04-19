n,k = map(int,input().split())

sigma_k = k * (k+1) // 2

n **= 2

answer = 0

for _ in range(2):
    if n >= sigma_k:
        n -= sigma_k
        answer += k
    
answer += n // k
answer += n % k

print(answer)
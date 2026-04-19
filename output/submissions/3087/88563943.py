def sigma(v):
    return v * (v+1) // 2

n,k = map(int,input().split())
if k > n : k = n
sigma_k = sigma(k)
n **= 2
answer = 0

if n >= sigma_k:
    n -= sigma_k
    answer += k
    
if n >= sigma_k:
    answer += k
    n -= sigma_k
    answer += n // k
    if n % k != 0: answer += 1
else:
    left, right = 0,k
    plus = 0
    while left <= right:
        mid  = (left+right) // 2
        if sigma(mid) >= n:
            plus = mid
            right = mid - 1
        else:
            left = mid + 1
    answer += plus 

print(answer)
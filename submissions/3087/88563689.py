n,k = map(int,input().split())
sigma_k = k * (k+1) // 2
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
        tmp = mid * (mid+1) // 2
        if tmp >= n:
            plus = mid
            right = mid - 1
        else:
            left = mid + 1
    answer += plus 

print(answer)
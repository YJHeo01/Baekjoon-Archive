import math

answer = 0

n = int(input())

array = [1] * (n+1)

prime_list = []

tmp = int(math.sqrt(n)+1)
for i in range(2,tmp):
    if array[i] == 1:
        prime_list.append(i)
        j = 2
        while i * j <= n:
            array[i*j] = 0
            j+=1
for i in range(tmp,n+1):
    if array[i] == 1:
        prime_list.append(i)

left, right = 0,0

prime_sum = 0

l = len(prime_list)
while right <= l:
    if prime_sum < n:
        if right == l:
            break
        prime_sum += prime_list[right]
        right+=1
    elif prime_sum == n:
        answer += 1
        prime_sum -= prime_list[left]
        left += 1
    else:
        prime_sum -= prime_list[left]
        left += 1 

print(answer)
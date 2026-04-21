INF = 1000001
prime = [True] * INF
prime_list = []
for i in range(2,INF):
    if prime[i] == True:
        prime_list.append(i)
        for j in range(i,INF,i):
            prime[j] = False
length = len(prime_list)
t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    left, right = 0,length-1
    while left <= right:
        if prime_list[left] + prime_list[right] > n:
            right -= 1
        elif prime_list[left] + prime_list[right] < n:
            left += 1
        else:
            answer += 1
            left += 1; right -= 1
    print(answer)
def zero_counter(n):
    answer = 0
    if n == 0:
        return 1
    while(1):
        if n % 10 == 0:
            answer += 1
            n = n / 10
        else : return answer
n = int(input())

for i in range(1,n):
    n = n * i

answer = zero_counter(n)

print(answer)
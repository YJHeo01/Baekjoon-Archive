n = int(input())

num = n

answer = 0

while True:
    answer += 1
    tmp = num // 10 + num % 10
    tmp = (num % 10) * 10 + tmp % 10
    if tmp == n: break
    num = tmp
    
print(answer)
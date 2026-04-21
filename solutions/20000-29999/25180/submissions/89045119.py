n = int(input())

answer = n // 9 + 1

if n % 2 != answer % 2: answer += 1

if n <= 9: answer = 1

print(answer)
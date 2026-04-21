n = int(input())

answer = [1] * n

for i in range(n//2):
    answer[n//2+i] = n - i * 2
    answer[n//2-1-i] = n - i * 2 - 1

print(*answer)
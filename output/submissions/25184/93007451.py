n = int(input())

answer = [n//2+1] * n

for i in range(n//2):
    answer[i*2] = n // 2 - i
    answer[i*2+1] = n - i
    
print(*answer)
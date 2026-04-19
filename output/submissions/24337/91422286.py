n,a,b = map(int,input().split())

answer = [1] * n

answer[n-b] = max(a,b)

for i in range(max(n-b,a)):
    answer[i] = i + 1

for i in range(b):
    if answer[n-i-1] != i + 1 and i != 0:
        print(-1)
        exit(0)
    if answer[n-i-1] == 1: answer[n-i-1] = i + 1
    
print(*answer)
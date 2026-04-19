n,a,b = map(int,input().split())

answer = [1] * n

for i in range(a):
    answer[i] = i + 1

for i in range(b):
    if answer[n-i-1] != i + 1 and i != 0:
        print(-1)
        exit(0)
    if answer[n-i-1] == 1: answer[n-i-1] = i + 1
    
print(*answer)
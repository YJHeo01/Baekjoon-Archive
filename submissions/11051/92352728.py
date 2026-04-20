n, k=map(int,input().split())

INF = 10007

answer = 1

for i in range(1,n+1):
    answer *= i
    
for i in range(1,k+1):
    answer //= i

for i in range(1,n-k+1):
    answer //= i

answer %= INF

print(answer)
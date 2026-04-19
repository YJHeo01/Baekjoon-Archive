n,m = map(int,input().split())
INF = int(1e13)
array = list(map(int,input().split()))
answer = 0
for i in range(1,n):
    if m > abs(array[i]-array[i-1]):
        array[i] += INF
        answer += 1
print(answer)
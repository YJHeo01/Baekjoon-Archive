a,b = map(int,input().split())
n = int(input())
array = [int(input()) for _ in range(n)]
answer = abs(a-b)
for i in array:
    answer = min(answer,abs(b-i)+1)
print(answer)
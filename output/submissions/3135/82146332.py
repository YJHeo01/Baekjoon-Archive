a,b = map(int,input().split())
int(input())
array = list(map(int,input().split()))
answer = abs(a-b)
for i in array:
    answer = min(answer,abs(b-i)+1)
print(answer)
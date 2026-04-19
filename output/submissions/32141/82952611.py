n,h = map(int,input().split())
array = list(map(int,input().split()))
answer = -1
for i in range(n):
    h -= array[i]
    if h <= 0:
        answer = i + 1
        break
print(answer)
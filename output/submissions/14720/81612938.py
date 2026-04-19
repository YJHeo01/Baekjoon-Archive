n = int(input())

array = list(map(int,input().split()))

idx = 0

answer = 0

for value in array:
    if value == idx:
        idx = (idx+1) % 3
        answer += 1

print(answer)
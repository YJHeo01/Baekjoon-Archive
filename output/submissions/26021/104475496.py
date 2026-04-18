n,k = map(int,input().split())

arr = list(input())

answer = k

for i in range(1,n):
    if arr[i-1] == arr[i]: answer -= 1

if arr[0] == 'R': answer -= 1

if answer < 0: answer = 0

print(answer)
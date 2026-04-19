n = int(input())
array= list(input())
answer = 0
idx = 0
while True:
    answer += 1
    if idx == n:
        break
    if array[idx] == 'S':
        idx += 1
    else:
        idx += 2

answer = min(answer,n)
    
print(answer)
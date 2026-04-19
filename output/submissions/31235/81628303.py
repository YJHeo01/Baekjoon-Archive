n = int(input())

array = list(map(int,input().split()))

answer = 0
max_value, max_idx = 0,-1

for i in range(n):
    if array[i] > max_value:
        answer = max(i-max_idx,answer)
        max_value = array[i]
        max_idx = i
    
print(answer)

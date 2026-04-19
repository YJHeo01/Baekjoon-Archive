n = int(input())

array = list(map(int,input().split()))

max_value = -1

answer = 0
move_max_value = -1
for i in range(n):
    if array[i] >= max_value:
        max_value = array[i]
    else:
        answer += 1
        move_max_value = max(move_max_value,array[i])

if array[i] < move_max_value:
    answer += 1
        
print(answer)
n = int(input())

array = list(map(int,input().split()))
array.reverse()

big = sorted(array,reverse=True)
answer = 0
move_max_value = -1
big_idx = 0

for i in range(n):
    if big[big_idx] == array[i]:
        big_idx += 1
    else:
        answer += 1
        
print(answer)
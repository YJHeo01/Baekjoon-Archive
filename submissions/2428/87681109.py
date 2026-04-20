n = int(input())

array = sorted(list(map(int,input().split())))

for i in range(n):
    array[i] *= 10
    
right = 0

answer = 0
for left in range(n):
    while True:
        if right >= n: break
        if array[right] * 9 // 10 > array[left]: break
        right += 1
    answer += (right-left-1)

print(answer)
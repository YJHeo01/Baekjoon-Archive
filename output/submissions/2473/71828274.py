n = int(input())

water = list(map(int,input().split()))

water.sort()
answer_value = int(1e9) 
answer = []

for i in range(n):
    fixed_water = water[i]
    left = 0
    right = n-1
    while 1:
        if left == i or right == i:
            break
        else:
            tmp = fixed_water + water[left] + water[right]
            if answer_value > abs(tmp):
                answer = [left,i,right]
                answer_value = abs(tmp)
            if tmp >= 0:
                right -= 1
            else:
                left += 1

answer.sort()

for i in answer:
    print(water[i],end=" ")
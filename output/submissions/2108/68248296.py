n = int(input())
array = []
cnt = [0]*8003
sum = 0
second = 0
for i in range(n):
    num = int(input())
    sum += num
    cnt[num] += 1
    array.append(num)
array.sort()
max_index = -4000
for i in range(-3999,4001):
    if cnt[max_index] < cnt[i]:
        max_index=i
        second = 0
    elif cnt[max_index] == cnt[i]:
        if second == 0:
            max_index=i
            second = 1



print(round(sum/n))
print(array[(n-1)//2])
print(max_index)
print(array[-1]-array[0])